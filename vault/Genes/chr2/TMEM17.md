---
symbol: "TMEM17"
type: "gene"
col: 11867
ensembl_id: "ENSG00000186889"
name: "transmembrane protein 17"
location: "2p15"
module: 94
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 47
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# TMEM17

*transmembrane protein 17* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.19× (z +7.7, q 8e-12, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.46× (z +3.7, q 0.038, up in 1 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.383× (z -6.6, q 2e-08, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM16L-1]] (+0.67, fdr 7e-06), [[SDSL]] (+0.65, fdr 7e-06), [[ZNF32]] (+0.64, fdr 1e-05); moves opposite to [[ODF2]] (-0.61, fdr 1e-05), [[EPN1]] (-0.58, fdr 4e-05), [[MXRA7]] (-0.56, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF480]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +7.7 | 8e-12 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +5.7 | 4e-06 | 4/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.038 | 1/40 (RKO) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +3.4 | 0.088 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +3.4 | 0.088 | 1/10 (PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.65×** | +3.3 | 0.088 | 2/25 (A549, PANC-1) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.59× | +3.1 | 0.17 | 1/6 (SW480) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.55× | +3.0 | 0.18 | 5/36 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11867.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.383×** | -6.6 | 2e-08 | 25/41 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.385×** | -6.6 | 2e-08 | 25/38 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.419×** | -6.0 | 5e-07 | 18/35 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.448×** | -5.5 | 5e-06 | 22/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.472×** | -5.2 | 3e-05 | 21/37 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -4.5 | 5e-04 | 17/31 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.565×** | -3.9 | 0.007 | 11/27 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.624×** | -3.2 | 0.087 | 12/40 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.417× | -3.1 | 0.11 | 12/33 (PANC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.640× | -3.1 | 0.12 | 11/19 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.02 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.112× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 3.33 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0517× (z -9.5) |
| [[SW480 (line)]] | alt | 2.93 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -8.7) |
| [[A-172 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.240 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.857 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.946 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.539 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.641 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.245 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16L-1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SDSL]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZNF32]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[METTL18]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[RSRC2]] | +0.61 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZNF391]] | +0.61 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[DHX36]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[FANCF]] | +0.59 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ARL14EP]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.58 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[ZNF625]] | +0.58 | +0.44 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF2]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[EPN1]] | -0.58 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MXRA7]] | -0.56 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[AP2A1]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[P3H1]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.53 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SETD3]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[EIF4EBP2]] | -0.53 | -0.25 / -0.61 | both halves | 4e-04 |  |
| [[GSDMB]] | -0.53 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[GNB2]] | -0.52 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[P4HB]] | -0.52 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ATP6AP2]] | -0.52 | -0.43 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TMEM17's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF480]] | C | ZNF480 activity raises TMEM17's level | lines that do not express ZNF480 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without ZNF480 | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: ZFP14, CIBAR1, ZNF540; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF480]] | C | TMEM17 activity raises ZNF480's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.85× lower at baseline in the lines without TMEM17 | 0.017 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; co-absent with the target |
| [[ZNF155]] | C | TMEM17 activity raises ZNF155's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 4.08× lower at baseline in the lines without TMEM17 | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| [[TCEAL1]] | C | TMEM17 activity raises TCEAL1's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without TMEM17 | 0.031 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | C | [[EID1]], TMEM17 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 1.29× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| [[TRIM68]] | C | TMEM17 activity raises TRIM68's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without TMEM17 | 0.040 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK; co-absent with the target |
| cells under [[Bendamustine (drug)]] 5 µM | C | [[EID1]], TMEM17 activity raises the cells' numbers under Bendamustine 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.77× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| cells under [[Epirubicin (hydrochloride) (drug)]] 0.5 µM | C | [[EID1]], TMEM17 activity lowers the cells' numbers under Epirubicin (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 1.26× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; co-absent genes |
| [[CD81]] | C | TMEM17 activity raises CD81's level | lines that do not express TMEM17 (3) vs lines expressing it (47) | 2.85× lower at baseline in the lines without TMEM17 | 0.089 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |
| cells under [[Nimesulide (drug)]] 5 µM | C | [[EID1]], TMEM17 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.74× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; cell counts less trustworthy; co-absent genes |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-30.3, 17.4); signed map (2.9, -21.6). **Vector** length 39.8, 5.22% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.8 | +1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:62,500,218-62,511,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34583 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X19](https://www.uniprot.org/uniprotkb/Q86X19) (Transmembrane protein 17):

> Transmembrane component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Required for ciliogenesis and sonic hedgehog/SHH signaling (By similarity).

**Summary**, from NCBI Gene [200728](https://www.ncbi.nlm.nih.gov/gene/200728):

> Involved in non-motile cilium assembly. Predicted to be located in ciliary membrane. Predicted to be part of MKS complex. Predicted to be active in ciliary transition zone. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26623) · Entrez [200728](https://www.ncbi.nlm.nih.gov/gene/200728) · UniProt [Q86X19](https://www.uniprot.org/uniprotkb/Q86X19) · Ensembl [ENSG00000186889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186889)

## Data

Gene col 11867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11867); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11867]; `tensor/DDL_lfc|DDL_z.npy` [11867]; `embed/gene_vectors.npy` [11867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11867 or target_col == 11867). Every well: [[TMEM17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

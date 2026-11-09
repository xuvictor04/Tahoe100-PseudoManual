---
symbol: "SLX4"
type: "gene"
col: 12055
ensembl_id: "ENSG00000188827"
name: "SLX4 structure-specific endonuclease subunit"
location: "16p13.3"
module: 22
arm: "+"
pooled_cpm: 13.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SLX4

*SLX4 structure-specific endonuclease subunit* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +13.4, q 2e-38, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.384× (z -11.7, q 7e-29, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPI]] (+0.65, fdr 1e-05), [[CCNF]] (+0.63, fdr 1e-05), [[ERCC6L]] (+0.61, fdr 7e-06); moves opposite to [[N4BP2L1]] (-0.66, fdr 3e-05), [[HSBP1L1]] (-0.66, fdr 1e-05), [[HPS1]] (-0.57, fdr 8e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +13.4 | 2e-38 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +12.9 | 1e-35 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +10.3 | 8e-23 | 43/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 0.001 | 17/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.051 | 9/48 (SNU-423, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.384×** | -11.7 | 7e-29 | 40/48 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -10.6 | 8e-24 | 37/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.487×** | -8.5 | 5e-15 | 32/43 (PANC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.528×** | -7.8 | 9e-13 | 34/47 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.677×** | -6.7 | 2e-09 | 24/48 (A498, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.577×** | -6.7 | 2e-09 | 29/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -6.7 | 2e-09 | 27/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.588×** | -6.1 | 7e-08 | 29/47 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.610×** | -6.0 | 1e-07 | 29/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -5.8 | 4e-07 | 24/47 (A-427, RPMI-7951, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.625×** | -5.5 | 2e-06 | 23/47 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -5.3 | 5e-06 | 26/47 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.688×** | -4.6 | 2e-04 | 18/36 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.1 | 0.001 | 22/47 (A549, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.003 | 20/46 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.003 | 19/48 (LOX-IMVI, SW 1088, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -3.9 | 0.003 | 19/48 (J82, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.727×** | -3.9 | 0.003 | 19/48 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.1 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.129× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.231× (z -10.9) |
| [[PANC-1 (line)]] | alt | 29.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.267× (z -12.6) |
| [[KATO III (line)]] | alt | 10.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.65× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.184× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.251× (z -8.8) |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.185× (z -9.4) |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -9.9) |
| [[A-172 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 9.77 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.222× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 5.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -8.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.163× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0584× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.27 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0503× (z -19.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 14.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -9.5) |
| [[A-427 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPI]] | +0.65 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CCNF]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ERCC6L]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[MSH5]] | +0.60 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[INCENP]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CEP55]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[KIFC1]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[H2AX]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair |
| [[BUB1]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZC3H10]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[HJURP]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NCAPH]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L1]] | -0.66 | -0.44 / -0.62 | both halves | 3e-05 |  |
| [[HSBP1L1]] | -0.66 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[HPS1]] | -0.57 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[C1orf54]] | -0.56 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[MAFG]] | -0.56 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ABRACL]] | -0.56 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[KLRD1]] | -0.56 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[N4BP2L2]] | -0.55 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[PRRG4]] | -0.55 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[MGAM]] | -0.54 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[RAB21]] | -0.54 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CCDC30]] | -0.54 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SLX4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-31.7, -57.0); signed map (-49.0, -39.4). **Vector** length 83.0, 17.1% of its response variance represented; |z| ≥ 3 in 1,152 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +12.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +13.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +10.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +1.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.5 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.1 | -3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -6.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | SLX4 structure-specific endonuclease subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,581,181-3,611,606 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1784, KIAA1987, FANCP; previously BTBD12 |
| Gene groups (HGNC) | FA complementation groups; BTB domain containing; Zinc fingers UBZ4 CCHC-type |
| Reactome | 8 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; Fanconi Anemia Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY92](https://www.uniprot.org/uniprotkb/Q8IY92) (Structure-specific endonuclease subunit SLX4):

> Regulatory subunit that interacts with and increases the activity of different structure-specific endonucleases. Has several distinct roles in protecting genome stability by resolving diverse forms of deleterious DNA structures originating from replication and recombination intermediates and from DNA damage. Component of the SLX1-SLX4 structure-specific endonuclease that resolves DNA secondary structures generated during DNA repair and recombination. Has endonuclease activity towards branched …

**Summary**, from NCBI Gene [84464](https://www.ncbi.nlm.nih.gov/gene/84464):

> This gene encodes a protein that functions as an assembly component of multiple structure-specific endonucleases. These endonuclease complexes are required for repair of specific types of DNA lesions and critical for cellular responses to replication fork failure. Mutations in this gene were found in patients with Fanconi anemia. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:23845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23845) · Entrez [84464](https://www.ncbi.nlm.nih.gov/gene/84464) · UniProt [Q8IY92](https://www.uniprot.org/uniprotkb/Q8IY92) · Ensembl [ENSG00000188827](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188827)

## Data

Gene col 12055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12055); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12055]; `tensor/DDL_lfc|DDL_z.npy` [12055]; `embed/gene_vectors.npy` [12055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12055 or target_col == 12055). Every well: [[SLX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

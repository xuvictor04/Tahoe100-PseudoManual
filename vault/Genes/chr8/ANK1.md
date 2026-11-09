---
symbol: "ANK1"
type: "gene"
col: 391
ensembl_id: "ENSG00000029534"
name: "ankyrin 1"
location: "8p11.21"
module: 80
arm: "+"
pooled_cpm: 10.39
n_lines_expressing: 28
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# ANK1

*ankyrin 1* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.75× (z +29.6, q 0e+00, up in 15 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.705× (z -4.7, q 0.002, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIA1]] (+0.65, fdr 1e-05), [[TM4SF18]] (+0.61, fdr 1e-05), [[CCDC190]] (+0.60, fdr 1e-05); moves opposite to [[RNF41]] (-0.47, fdr 2e-04), [[ZXDC]] (-0.46, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[APOBEC3C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 391.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.75×** | +29.6 | 0e+00 | 15/21 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.92×** | +18.3 | 0e+00 | 17/19 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +15.5 | 0e+00 | 12/22 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.28×** | +15.3 | 0e+00 | 8/10 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +13.0 | 8e-37 | 8/12 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +8.9 | 5e-17 | 10/20 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.92×** | +8.8 | 2e-16 | 10/23 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +8.3 | 7e-15 | 13/25 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.3 | 1e-14 | 7/23 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 2e-11 | 7/25 (A549, A498, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +6.5 | 4e-09 | 1/11 (J82) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.1 | 5e-08 | 5/24 (HOP62, SW480, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.56×** | +5.5 | 1e-06 | 3/22 (Panc 03.27, SHP-77, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.41×** | +4.5 | 3e-04 | 7/24 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 9e-04 | 6/22 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 7/21 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.003 | 5/25 (A549, SW480, …) | top dose only |  |
| [[Menadione (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.039 | 2/23 (Panc 03.27, HS-578T) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.048 | 8/25 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.085 | 1/23 (J82) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 391.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.705×** | -4.7 | 0.002 | 12/25 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.726×** | -4.3 | 0.005 | 9/25 (A-172, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.806×** | -4.1 | 0.008 | 9/25 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.745×** | -4.0 | 0.011 | 13/24 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.059 | 6/25 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.775×** | -3.4 | 0.059 | 5/25 (HS-578T, Hs 766T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.788× | -3.2 | 0.11 | 5/25 (Hs 766T, RPMI-7951, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.792× | -3.1 | 0.11 | 3/25 (NCI-H661, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.793× | -3.1 | 0.11 | 8/25 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.798× | -3.0 | 0.14 | 4/25 (HOP62, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 391. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 81.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.4) |
| [[A-172 (line)]] | wt | 45.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.274× (z -9.6) |
| [[Hs 766T (line)]] | wt | 99.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.340× (z -8.8) |
| [[HOP62 (line)]] | alt | 2.73 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +9.5) | — |
| [[LoVo (line)]] | wt | 5.31 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.88× (z +11.7) | — |
| [[A-427 (line)]] | wt | 8.14 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0503× (z -12.3) |
| [[A498 (line)]] | wt | 2.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +9.7) | — |
| [[A549 (line)]] | wt | 3.10 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.35× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 4.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 391), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIA1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[TM4SF18]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CCDC190]] | +0.60 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GFRA1]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[DPY19L2P2]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[CFAP54]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[LINC02966]] | +0.55 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[EFCAB5]] | +0.54 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[BHLHE40-AS1]] | +0.54 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[SPOCK3]] | +0.54 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[RAD9B]] | +0.54 | +0.52 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF41]] | -0.47 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[ZXDC]] | -0.46 | -0.32 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.3% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOBEC3C]] | B | ANK1 activity raises APOBEC3C's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without ANK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent |
| [[CACNG2]] | B | ANK1 activity raises CACNG2's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without ANK1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent |
| [[DSC3]] | C | ANK1 activity raises DSC3's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 2.05× lower at baseline in the lines without ANK1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.3, 19.4); signed map (42.5, 19.2). **Vector** length 62.6, 14.6% of its response variance represented; |z| ≥ 3 in 652 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +29.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:41,653,220-41,896,741 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPH1; previously ANK |
| Gene groups (HGNC) | MicroRNA protein coding host genes; ZU5 domain containing ; Ankyrin family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 13 pathways, smallest: Neurofascin interactions; NrCAM interactions; CHL1 interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P16157](https://www.uniprot.org/uniprotkb/P16157) (Ankyrin-1):

> Component of the ankyrin-1 complex, a multiprotein complex involved in the stability and shape of the erythrocyte membrane. Attaches integral membrane proteins to cytoskeletal elements; binds to the erythrocyte membrane protein band 4.2, to Na-K ATPase, to the lymphocyte membrane protein GP85, and to the cytoskeletal proteins fodrin, tubulin, vimentin and desmin. Erythrocyte ankyrins also link spectrin (beta chain) to the cytoplasmic domain of the erythrocytes anion exchange protein; they …

**Summary**, from NCBI Gene [286](https://www.ncbi.nlm.nih.gov/gene/286):

> Ankyrins are a family of proteins that link the integral membrane proteins to the underlying spectrin-actin cytoskeleton and play key roles in activities such as cell motility, activation, proliferation, contact and the maintenance of specialized membrane domains. Multiple isoforms of ankyrin with different affinities for various target proteins are expressed in a tissue-specific, developmentally regulated manner. Most ankyrins are typically composed of three structural domains: an …

**Accessions** — [HGNC:492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:492) · Entrez [286](https://www.ncbi.nlm.nih.gov/gene/286) · UniProt [P16157](https://www.uniprot.org/uniprotkb/P16157) · Ensembl [ENSG00000029534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000029534)

## Data

Gene col 391: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 391); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 391, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 391]; `tensor/DDL_lfc|DDL_z.npy` [391]; `embed/gene_vectors.npy` [391]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 391 or target_col == 391). Every well: [[ANK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

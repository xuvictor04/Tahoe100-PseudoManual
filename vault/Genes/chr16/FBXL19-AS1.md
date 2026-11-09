---
symbol: "FBXL19-AS1"
type: "gene"
col: 15305
ensembl_id: "ENSG00000260852"
name: "FBXL19 antisense RNA 1"
location: "16p11.2"
module: 26
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# FBXL19-AS1

*FBXL19 antisense RNA 1* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.21× (z +12.3, q 7e-32, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.377× (z -10.3, q 5e-22, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC90B-AS1]] (+0.84, fdr 7e-06), [[AKT1S1]] (+0.78, fdr 7e-06), [[PTOV1-AS1]] (+0.78, fdr 7e-06); moves opposite to [[POGLUT2]] (-0.69, fdr 1e-05), [[ATG4C]] (-0.67, fdr 3e-05), [[ARL3]] (-0.67, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.21×** | +12.3 | 7e-32 | 39/44 (BT-474, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +11.8 | 9e-30 | 3/3 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +10.3 | 1e-22 | 6/7 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.2 | 3e-22 | 18/24 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +10.0 | 3e-21 | 25/39 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +8.6 | 7e-16 | 20/38 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.98×** | +7.2 | 5e-11 | 24/43 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.8 | 9e-10 | 19/38 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.87×** | +6.6 | 3e-09 | 22/43 (HOP62, LoVo, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +5.8 | 4e-07 | 16/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.7 | 7e-07 | 16/46 (A-172, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +5.5 | 2e-06 | 18/47 (LS 180, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +4.8 | 7e-05 | 11/47 (LoVo, MIA PaCa-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.57×** | +4.5 | 3e-04 | 12/42 (COLO 205, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 5e-04 | 11/44 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **2.09×** | +4.1 | 0.002 | 3/38 (BT-474, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.005 | 5/46 (H4, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.015 | 8/36 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.088 | 4/47 (PANC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.377×** | -10.3 | 5e-22 | 33/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.380×** | -10.2 | 5e-22 | 34/47 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -9.3 | 2e-18 | 34/45 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.552×** | -6.3 | 5e-08 | 26/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.700×** | -5.3 | 1e-05 | 20/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.425×** | -4.7 | 2e-04 | 16/43 (RPMI-7951, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.668×** | -4.3 | 0.002 | 15/40 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.919× | -3.1 | 0.13 | 13/48 (HepG2/C3A, A-172, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.750× | -3.0 | 0.15 | 12/40 (SHP-77, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.52 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0802× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 6.86 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0413× (z -10.2) |
| [[LS 180 (line)]] | wt | 4.37 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0755× (z -9.0) |
| [[SW480 (line)]] | alt | 4.62 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.168× (z -8.8) |
| [[A-172 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | +0.84 | +0.73 / +0.67 | both halves | 7e-06 | same gene group |
| [[AKT1S1]] | +0.78 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PTOV1-AS1]] | +0.78 | +0.65 / +0.73 | both halves | 7e-06 | same gene group |
| [[CATSPERE]] | +0.78 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[NQO1-DT]] | +0.77 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.74 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[LINC00571]] | +0.74 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[C2orf49-DT]] | +0.74 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ACYP2]] | +0.72 | +0.68 / +0.39 | both halves | 5e-05 |  |
| [[PHF8]] | +0.72 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SUMO2P17]] | +0.72 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NEK11]] | +0.71 | +0.57 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POGLUT2]] | -0.69 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ATG4C]] | -0.67 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ARL3]] | -0.67 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[LCMT1]] | -0.67 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[NBPF3]] | -0.67 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.65 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ELP1]] | -0.65 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[HEATR5B]] | -0.64 | -0.58 / -0.26 | both halves | 4e-04 |  |
| [[YIF1B]] | -0.64 | -0.54 / -0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[SDHAF3]] | -0.64 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TAMM41]] | -0.64 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[ABHD10]] | -0.64 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MMS19]] | -0.63 | -0.67 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FBXL19-AS1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises FBXL19-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (9.4, 12.5); signed map (24.0, -4.4). **Vector** length 71.8, 11.2% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.4 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -9.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -10.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -1.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | FBXL19 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p11.2 — chr16:30,919,319-30,923,269 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC125469, MGC125470, MGC125472; previously NCRNA00095 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q494R0](https://www.uniprot.org/uniprotkb/Q494R0) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27557) · Entrez [283932](https://www.ncbi.nlm.nih.gov/gene/283932) · UniProt [Q494R0](https://www.uniprot.org/uniprotkb/Q494R0) · Ensembl [ENSG00000260852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260852)

## Data

Gene col 15305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15305); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15305]; `tensor/DDL_lfc|DDL_z.npy` [15305]; `embed/gene_vectors.npy` [15305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15305 or target_col == 15305). Every well: [[FBXL19-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL19-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

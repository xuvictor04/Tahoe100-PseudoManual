---
symbol: "CENPT"
type: "gene"
col: 2288
ensembl_id: "ENSG00000102901"
name: "centromere protein T"
location: "16q22.1"
module: 2
arm: "+"
pooled_cpm: 13.19
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 7
n_dd_up_clean: 24
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CENPT

*centromere protein T* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.39× (z +24.7, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.672× (z -8.1, q 4e-13, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HGS]] (+0.56, fdr 1e-05), [[ALKBH6]] (+0.55, fdr 3e-05), [[GUCD1]] (+0.55, fdr 4e-05); moves opposite to [[GTF2H5]] (-0.51, fdr 2e-04), [[UBA2]] (-0.50, fdr 4e-05), [[ST3GAL5]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2288.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.39×** | +24.7 | 0e+00 | 44/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +10.3 | 1e-22 | 36/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.3 | 1e-22 | 33/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.98×** | +9.8 | 2e-20 | 35/47 (SW480, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +7.7 | 1e-12 | 35/48 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +7.1 | 2e-10 | 28/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.57×** | +6.4 | 9e-09 | 24/48 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.52×** | +5.8 | 5e-07 | 13/24 (NCI-H460, SW1417, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.8 | 5e-07 | 17/30 (SW1417, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.4 | 4e-06 | 23/48 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.38×** | +4.6 | 2e-04 | 19/47 (LoVo, BT-474, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.40×** | +4.6 | 2e-04 | 20/47 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.35×** | +4.3 | 7e-04 | 17/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 18/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.002 | 13/48 (NCI-H460, HOP62, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.004 | 14/47 (LoVo, SNU-1, …) | all doses, flat | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.005 | 11/45 (CFPAC-1, Panc 03.27, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.012 | 10/48 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.024 | 9/48 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.024 | 9/44 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2288.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.672×** | -8.1 | 4e-13 | 27/47 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.710×** | -6.9 | 1e-09 | 30/48 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.473×** | -5.6 | 4e-06 | 20/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.509×** | -5.1 | 6e-05 | 19/44 (BT-474, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.711×** | -4.9 | 1e-04 | 20/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.729×** | -4.5 | 6e-04 | 21/47 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.753×** | -3.9 | 0.007 | 15/47 (AsPC-1, LOX-IMVI, …) | top dose only | composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2288. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 20.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 12.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +10.6) | [[Silodosin (drug)]] 5 µM 0.100× (z -12.2) |
| [[A-427 (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +14.3) | — |
| [[A549 (line)]] | wt | 8.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +13.1) | — |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.7) |
| [[C32 (line)]] | wt | 9.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 8.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.4) | — |
| [[J82 (line)]] | alt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[KATO III (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.2) | — |
| [[LoVo (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.84× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.427× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 7.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 33.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 8.92 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 5.34 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.174× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +17.1) | — |
| [[Panc 03.27 (line)]] | alt | 9.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 6.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.5) | — |
| [[RKO (line)]] | wt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 9.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +10.4) | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0841× (z -9.2) |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2288), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HGS]] | +0.56 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ALKBH6]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[GUCD1]] | +0.55 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[TP53I13]] | +0.55 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[FAM219A]] | +0.53 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[APH1A]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[PTRH1]] | +0.52 | +0.26 / +0.58 | both halves | 4e-04 |  |
| [[MTCH1]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZFYVE21]] | +0.51 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[MIEF2]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[TMEM234]] | +0.51 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RAB5B]] | +0.51 | +0.40 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H5]] | -0.51 | -0.59 / -0.31 | both halves | 2e-04 |  |
| [[UBA2]] | -0.50 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[ST3GAL5]] | -0.49 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[CAAP1]] | -0.49 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[INIP]] | -0.48 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[TMEM251]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MSL3P1]] | -0.47 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ZNF45]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[BIRC3]] | -0.47 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[SMIM30]] | -0.46 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PPP4R2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[DDX19B]] | -0.46 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CENPT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.367). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-14.6, -16.0); signed map (-23.4, 1.7). **Vector** length 95.5, 20.2% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +24.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +9.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +10.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.0 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.5 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein T |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,828,157-67,847,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13111, CENP-T; previously C16orf56 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BT3](https://www.uniprot.org/uniprotkb/Q96BT3) (Centromere protein T):

> Component of the CENPA-NAC (nucleosome-associated) complex, a complex that plays a central role in assembly of kinetochore proteins, mitotic progression and chromosome segregation. The CENPA-NAC complex recruits the CENPA-CAD (nucleosome distal) complex and may be involved in incorporation of newly synthesized CENPA into centromeres. Part of a nucleosome-associated complex that binds specifically to histone H3-containing nucleosomes at the centromere, as opposed to nucleosomes containing CENPA. …

**Summary**, from NCBI Gene [80152](https://www.ncbi.nlm.nih.gov/gene/80152):

> The centromere is a specialized chromatin domain, present throughout the cell cycle, that acts as a platform on which the transient assembly of the kinetochore occurs during mitosis. All active centromeres are characterized by the presence of long arrays of nucleosomes in which CENPA (MIM 117139) replaces histone H3 (see MIM 601128). CENPT is an additional factor required for centromere assembly (Foltz et al., 2006 [PubMed 16622419]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25787) · Entrez [80152](https://www.ncbi.nlm.nih.gov/gene/80152) · UniProt [Q96BT3](https://www.uniprot.org/uniprotkb/Q96BT3) · Ensembl [ENSG00000102901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102901)

## Data

Gene col 2288: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2288); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2288, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2288]; `tensor/DDL_lfc|DDL_z.npy` [2288]; `embed/gene_vectors.npy` [2288]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2288 or target_col == 2288). Every well: [[CENPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

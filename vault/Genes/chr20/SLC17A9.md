---
symbol: "SLC17A9"
type: "gene"
col: 2093
ensembl_id: "ENSG00000101194"
name: "solute carrier family 17 member 9"
location: "20q13.33"
module: 2
arm: "+"
pooled_cpm: 7.84
n_lines_expressing: 23
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# SLC17A9

*solute carrier family 17 member 9* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.40× (z +8.7, q 2e-15, up in 4 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +6.7, q 2e-09, up in 0 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.622× (z -4.7, q 0.001, down in 9 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPCN2]] (+0.64, fdr 1e-05), [[ARFGAP1]] (+0.62, fdr 1e-05), [[IGSF9]] (+0.61, fdr 3e-05); moves opposite to [[NIPBL]] (-0.51, fdr 4e-05), [[SETD2]] (-0.50, fdr 6e-05), [[TLK2]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC38A5]] → it (grade C ⚠); 4 go from it, the strongest it → [[NGEF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.7 | 2e-15 | 4/16 (HepG2/C3A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +7.7 | 5e-12 | 2/12 (HepG2/C3A, HT-29) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.8 | 2e-09 | 3/14 (HepG2/C3A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +6.7 | 2e-09 | 0/20 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.89×** | +4.5 | 7e-04 | 8/19 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +4.1 | 0.004 | 13/21 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.7 | 0.017 | 5/12 (KATO III, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.1 | 0.13 | 4/20 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.13 | 6/21 (HS-578T, KATO III, …) | inconsistent across doses | position effect removed |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.13 | 11/21 (HS-578T, KATO III, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.13 | 8/19 (Panc 03.27, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.7 | 0.001 | 9/21 (KATO III, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -4.4 | 0.003 | 12/21 (RPMI-7951, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.638×** | -4.3 | 0.003 | 15/21 (HS-578T, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -4.3 | 0.003 | 8/21 (KATO III, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.694×** | -3.6 | 0.030 | 5/21 (LoVo, SW48, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.782×** | -3.5 | 0.050 | 17/20 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -3.3 | 0.069 | 3/21 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.804× | -3.1 | 0.15 | 4/21 (RKO, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0779× (z -21.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -13.1) |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.1) |
| [[KATO III (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.1) |
| [[SW480 (line)]] | alt | 26.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~59% of this change |
| [[COLO 205 (line)]] | alt | 7.00 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0587× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0734× (z -10.3) |
| [[LS 180 (line)]] | wt | 7.58 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.223× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 4.32 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0706× (z -9.2) |
| [[RKO (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -16.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.647 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.850 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.736 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPCN2]] | +0.64 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[IGSF9]] | +0.61 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[SH3BP2]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[PRR5]] | +0.57 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[GPSM1]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[TNFRSF25]] | +0.56 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[INF2]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[IGSF9B]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[NSMF]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PYCR1]] | +0.53 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[AMPD2]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPBL]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[SETD2]] | -0.50 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[TLK2]] | -0.50 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[TLK1]] | -0.47 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[CLPX]] | -0.47 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[DCUN1D1]] | -0.47 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[LSM14A]] | -0.47 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[RNF115]] | -0.46 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[DPY19L1P1]] | -0.45 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[MTUS1-DT]] | -0.45 | -0.47 / -0.23 | both halves | 5e-04 |  |
| [[YY1]] | -0.45 | -0.41 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC38A5]] | C | SLC38A5 activity raises SLC17A9's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 3.30× lower at baseline in the lines without SLC38A5 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NGEF]] | B | SLC17A9 activity raises NGEF's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 2.18× lower at baseline in the lines without SLC17A9 | 0.085 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22 |
| [[NIPBL]] | B | SLC17A9 activity lowers NIPBL's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 1.15× higher at baseline in the lines without SLC17A9 | 0.095 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22 |
| [[SLC38A5]] | C | SLC17A9 activity raises SLC38A5's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 2.82× lower at baseline in the lines without SLC17A9 | 0.012 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22; co-absent with the target |
| [[TINAGL1]] | C | SLC17A9 activity raises TINAGL1's level | lines that do not express SLC17A9 (27) vs lines expressing it (23) | 3.97× lower at baseline in the lines without SLC17A9 | 0.033 | ⚠ within organs, on part of the lines; also absent: UGT1A9, MT1G, TTC22; co-absent with the target |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (14.8, -4.6); signed map (-11.9, 30.5). **Vector** length 51.3, 13.0% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.4 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -4.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 17 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,952,707-62,969,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23412, VNUT; previously C20orf59 |
| Gene groups (HGNC) | Solute carrier family 17 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYT1](https://www.uniprot.org/uniprotkb/Q9BYT1) (Voltage-gated purine nucleotide uniporter SLC17A9):

> Voltage-gated ATP nucleotide uniporter that can also transport the purine nucleotides ADP and GTP. Uses the membrane potential as the driving force to control ATP accumulation in lysosomes and secretory vesicles. By controlling ATP storage in lysosomes, regulates ATP-dependent proteins of these organelles. Also indirectly regulates the exocytosis of ATP through its import into lysosomes in astrocytes and secretory vesicles such as adrenal chromaffin granules, mucin granules and synaptic …

**Summary**, from NCBI Gene [63910](https://www.ncbi.nlm.nih.gov/gene/63910):

> This gene encodes a member of a family of transmembrane proteins that are involved in the transport of small molecules. The encoded protein participates in the vesicular uptake, storage, and secretion of adenoside triphosphate (ATP) and other nucleotides. A mutation in this gene was found in individuals with autosomal dominant disseminated superficial actinic porokeratosis-8. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:16192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16192) · Entrez [63910](https://www.ncbi.nlm.nih.gov/gene/63910) · UniProt [Q9BYT1](https://www.uniprot.org/uniprotkb/Q9BYT1) · Ensembl [ENSG00000101194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101194)

## Data

Gene col 2093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2093); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2093]; `tensor/DDL_lfc|DDL_z.npy` [2093]; `embed/gene_vectors.npy` [2093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2093 or target_col == 2093). Every well: [[SLC17A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC17A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

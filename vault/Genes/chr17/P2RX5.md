---
symbol: "P2RX5"
type: "gene"
col: 1370
ensembl_id: "ENSG00000083454"
name: "purinergic receptor P2X 5"
location: "17p13.2"
module: 5
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 35
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# P2RX5

*purinergic receptor P2X 5* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.15× (z +13.6, q 3e-39, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +10.2, q 2e-22, up in 9 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (RKO 0.0689×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (LoVo 0.0481×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.335×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPNE7]] (+0.68, fdr 7e-06), [[SLC25A15]] (+0.66, fdr 7e-06), [[TRIM65]] (+0.65, fdr 7e-06); moves opposite to [[GABARAP]] (-0.56, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[CFAP36]] (-0.53, fdr 1e-05), [[GABARAPL2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GAL]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GAL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +13.6 | 3e-39 | 7/9 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.59×** | +11.3 | 6e-27 | 5/7 (A-172, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +10.3 | 1e-22 | 3/4 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.2 | 2e-22 | 9/24 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.8 | 2e-09 | 6/12 (SW480, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.92×** | +6.2 | 5e-08 | 6/24 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +5.8 | 5e-07 | 9/25 (SW480, Panc 03.27, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.60×** | +4.5 | 6e-04 | 8/29 (SW480, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +4.3 | 0.001 | 12/30 (SW480, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.008 | 4/27 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **1.49×** | +3.8 | 0.009 | 3/25 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.6 | 0.013 | 4/18 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.5 | 0.017 | 2/16 (RKO, NCI-H23) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.020 | 2/25 (SW480, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.020 | 1/17 (A549) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.034 | 3/28 (NCI-H1792, HEC-1-A, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.037 | 1/16 (PANC-1) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.049 | 2/16 (SW480, NCI-H2347) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.066 | 1/28 (A498) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.075 | 4/28 (MIA PaCa-2, A-172, …) | inconsistent across doses | position effect removed |
| [[Rosiglitazone (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.081 | 4/21 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1370.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (RKO 0.0689×); [[Procainamide (hydrochloride) (drug)]] 0.5 µM in 1 line (LoVo 0.0481×); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.335×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.5 µM |  | 0.704× | -3.4 | 0.42 | 3/27 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.757× | -3.1 | 0.50 | 5/29 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 2.62 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0481× (z -9.6) |
| [[PANC-1 (line)]] | alt | 6.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.3) |
| [[RKO (line)]] | wt | 9.66 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0689× (z -11.1) |
| [[SW480 (line)]] | alt | 7.71 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.56× (z +8.7) | — |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.701 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.970 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.549 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.326 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.384 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.636 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.515 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPNE7]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A15]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TRIM65]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ZNF485]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[LETM1]] | +0.63 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[TBRG4]] | +0.62 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZNF121]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[PUS1]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[WDR4]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[WDR77]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 | STRING 493 |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | -0.56 | -0.49 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CFAP36]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL]] | B | GAL activity raises P2RX5's level | lines that do not express GAL (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without GAL | 0.003 | ⚠ within organs, on part of the lines; also absent: HEYL, ACP7, SEC14L4 |
| [[BEGAIN]] | B | BEGAIN activity raises P2RX5's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 1.76× lower at baseline in the lines without BEGAIN | 0.059 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[SNHG26]] | B | SNHG26 activity raises P2RX5's level | lines that do not express SNHG26 (11) vs lines expressing it (39) | 1.79× lower at baseline in the lines without SNHG26 | 0.067 | ⚠ within organs, on part of the lines; also absent: HEG1, GPR63, FAM171A1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAL]] | B | P2RX5 activity raises GAL's level | lines that do not express P2RX5 (15) vs lines expressing it (35) | 2.51× lower at baseline in the lines without P2RX5 | 0.007 | ⚠ within organs, on part of the lines; also absent: C1orf115, LIMS2, PALM |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-9.6, -36.0); signed map (-2.1, -53.7). **Vector** length 43.0, 6.81% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.51 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +13.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.0 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | purinergic receptor P2X 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,672,199-3,696,240 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P2X5, LRH-1 |
| Gene groups (HGNC) | Purinergic receptors P2X; Minor histocompatibility antigens |
| Reactome | 4 pathways, smallest: Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93086](https://www.uniprot.org/uniprotkb/Q93086) (P2X purinoceptor 5):

> [Isoform 6]: ATP-gated nonselective transmembrane cation channel permeable to potassium, sodium and calcium. Unlike other P2RX receptors, the P2X5 receptor is also permeable to chloride. May play a supporting role in the inflammatory response (By similarity).; [Isoform 1]: Non-functional.

**Summary**, from NCBI Gene [5026](https://www.ncbi.nlm.nih.gov/gene/5026):

> The product of this gene belongs to the family of purinoceptors for ATP. This receptor functions as a ligand-gated ion channel. Alternative splicing results in multiple transcript variants. Read-through transcription also exists between this gene and the neighboring downstream gene, TAX1BP3 (Tax1 binding protein 3). [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:8536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8536) · Entrez [5026](https://www.ncbi.nlm.nih.gov/gene/5026) · UniProt [Q93086](https://www.uniprot.org/uniprotkb/Q93086) · Ensembl [ENSG00000083454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083454)

## Data

Gene col 1370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1370); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1370]; `tensor/DDL_lfc|DDL_z.npy` [1370]; `embed/gene_vectors.npy` [1370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1370 or target_col == 1370). Every well: [[P2RX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

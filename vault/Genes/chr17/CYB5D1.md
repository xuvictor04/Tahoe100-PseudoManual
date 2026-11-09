---
symbol: "CYB5D1"
type: "gene"
col: 11262
ensembl_id: "ENSG00000182224"
name: "cytochrome b5 domain containing 1"
location: "17p13.1"
module: 54
arm: "-"
pooled_cpm: 10.38
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CYB5D1

*cytochrome b5 domain containing 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.70× (z +33.6, q 0e+00, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.664× (z -7.9, q 2e-12, down in 30 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF543]] (+0.67, fdr 1e-05), [[ZNF34]] (+0.67, fdr 1e-05), [[RLIM]] (+0.65, fdr 1e-05); moves opposite to [[RNF149]] (-0.67, fdr 7e-06), [[BLVRA]] (-0.66, fdr 1e-05), [[RECK]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.70×** | +33.6 | 0e+00 | 40/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +14.9 | 0e+00 | 34/41 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +13.3 | 3e-38 | 35/41 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.33×** | +11.1 | 2e-26 | 33/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +9.2 | 5e-18 | 17/26 (A549, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.72×** | +7.1 | 1e-10 | 11/19 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +6.9 | 4e-10 | 26/44 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.50×** | +5.6 | 2e-06 | 16/35 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +4.1 | 0.003 | 16/45 (SNU-1, A-172, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.005 | 20/45 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +3.5 | 0.023 | 14/43 (RKO, NCI-H23, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.068 | 8/46 (HOP62, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.084 | 3/46 (RPMI-7951, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.25× | +3.0 | 0.11 | 8/45 (J82, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.664×** | -7.9 | 2e-12 | 30/46 (HS-578T, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.642×** | -6.1 | 4e-07 | 24/44 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.685×** | -4.9 | 2e-04 | 18/45 (NCI-H2030, SNU-1, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **0.743×** | -4.1 | 0.007 | 14/43 (AN3 CA, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.782×** | -3.4 | 0.091 | 13/44 (J82, SW 900, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.848× | -3.1 | 0.21 | 9/46 (C32, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.51 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.0× (z +20.5) | [[Simotinib (drug)]] 5 µM 0.114× (z -10.5) ⚠ toxic · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.120× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 9.38 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +26.5) | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +18.0) | — |
| [[PANC-1 (line)]] | alt | 8.13 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +18.0) | — |
| [[A498 (line)]] | wt | 14.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.04× (z +20.8) | — |
| [[C32 (line)]] | wt | 12.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.43× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 7.03 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +12.8) | [[Tucidinostat (drug)]] 0.5 µM 0.0985× (z -9.3) |
| [[HS-578T (line)]] | alt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +18.6) | — |
| [[hTERT-HPNE (line)]] | wt | 7.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +14.8) | — |
| [[J82 (line)]] | alt | 12.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.314× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +14.4) | — |
| [[A549 (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 7.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.8) | — |
| [[COLO 205 (line)]] | alt | 4.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +15.3) | — |
| [[HOP62 (line)]] | alt | 7.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +20.5) | — |
| [[KATO III (line)]] | alt | 6.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +9.6) | — |
| [[LoVo (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.77× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.144× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 7.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.7× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 9.92 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.1× (z +19.5) | — |
| [[SW 900 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +13.9) | — |
| [[SW480 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.3) | — |
| [[A-427 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF543]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZNF34]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[RLIM]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[RGL2]] | +0.64 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[THOC6]] | +0.63 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ZNF597]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[CYREN]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[TASOR]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.62 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[ZNF436]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC13]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF149]] | -0.67 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[BLVRA]] | -0.66 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[RECK]] | -0.66 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[TRPC4AP]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[STK38]] | -0.64 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.63 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[NENF]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 | same gene group |
| [[LMTK2]] | -0.60 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.59 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[CDC42SE2]] | -0.59 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[SEC24B]] | -0.59 | -0.67 / -0.39 | both halves | 6e-05 |  |
| [[RPS24]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises CYB5D1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.43× lower at baseline in the lines without TSPAN33 | 0.068 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SESTD1]] | C | SESTD1 activity lowers CYB5D1's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.76× higher at baseline in the lines without SESTD1 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.5, 1.2); signed map (14.1, -8.8). **Vector** length 80.0, 14.4% of its response variance represented; |z| ≥ 3 in 1,027 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +33.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +13.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +14.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.3 | +2.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.3 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -6.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.4 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,857,746-7,862,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32499 |
| Gene groups (HGNC) | Cytochrome b5 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9G0](https://www.uniprot.org/uniprotkb/Q6P9G0) (Cytochrome b5 domain-containing protein 1):

> Radial spoke stalk protein that binds heme under oxidizing conditions. Required for the coordinated beating of multiple cilia maybe by functioning in a redox signaling pathway.

**Summary**, from NCBI Gene [124637](https://www.ncbi.nlm.nih.gov/gene/124637):

> Predicted to enable metal ion binding activity. Predicted to be involved in cilium movement and regulation of cilium beat frequency. Predicted to be located in axoneme and sperm flagellum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26516) · Entrez [124637](https://www.ncbi.nlm.nih.gov/gene/124637) · UniProt [Q6P9G0](https://www.uniprot.org/uniprotkb/Q6P9G0) · Ensembl [ENSG00000182224](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182224)

## Data

Gene col 11262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11262); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11262]; `tensor/DDL_lfc|DDL_z.npy` [11262]; `embed/gene_vectors.npy` [11262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11262 or target_col == 11262). Every well: [[CYB5D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

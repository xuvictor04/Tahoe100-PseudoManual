---
symbol: "CELSR3"
type: "gene"
col: 167
ensembl_id: "ENSG00000008300"
name: "cadherin EGF LAG seven-pass G-type receptor 3"
location: "3p21.31"
module: 96
arm: "+"
pooled_cpm: 8.2
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# CELSR3

*cadherin EGF LAG seven-pass G-type receptor 3* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.62× (z +19.0, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -4.6, q 0.002, down in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.230×, MIA PaCa-2 0.213×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (BT-474 0.0807×, A-427 0.137×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0860×; ⚠ cell-cycle shift, explains ~16% of this change); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0536×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (C-33 A 0.0953×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THOC6]] (+0.79, fdr 7e-06), [[SRRM2]] (+0.74, fdr 7e-06), [[SCAF1]] (+0.74, fdr 7e-06); moves opposite to [[RNF149]] (-0.66, fdr 1e-05), [[NDUFAF7]] (-0.65, fdr 7e-06), [[NENF]] (-0.63, fdr 9e-06).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF32-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 167.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.62×** | +19.0 | 0e+00 | 39/42 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +7.9 | 5e-13 | 30/42 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +6.1 | 3e-07 | 25/43 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.0 | 0.010 | 7/15 (A-172, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.9 | 0.013 | 9/22 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.038 | 14/45 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.049 | 7/46 (PANC-1, HT-29, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.092 | 13/43 (HOP62, SW48, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.2 | 0.094 | 12/31 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.12 | 12/45 (NCI-H460, NCI-H2030, …) | rises with dose | position effect removed |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.41× | +3.0 | 0.12 | 6/45 (HEC-1-A, C32, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.41× | +3.0 | 0.12 | 12/43 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 167.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.230×, MIA PaCa-2 0.213×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (BT-474 0.0807×, A-427 0.137×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (C-33 A 0.0860×; ⚠ cell-cycle shift, explains ~16% of this change); [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0536×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (C-33 A 0.0953×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -4.6 | 0.002 | 21/44 (C-33 A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.611×** | -4.3 | 0.004 | 21/42 (RPMI-7951, Panc 03.27, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.870× | -4.1 | 0.009 | 21/46 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -4.0 | 0.010 | 21/42 (C-33 A, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ribociclib (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.708× | -3.0 | 0.26 | 7/45 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 167. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 24.1 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0860× (z -11.6) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.0953× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 2.85 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.5× (z +20.0) | — |
| [[SNU-1 (line)]] | wt | 17.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +10.5) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0843× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Hesperidin (drug)]] 0.05 µM 0.0838× (z -9.3) |
| [[A-427 (line)]] | wt | 15.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.85× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.137× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 8.75 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.14× (z +13.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 7.60 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0947× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 9.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.27× (z +13.2) | [[Canagliflozin (drug)]] 0.05 µM 0.101× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 2 | — | [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM 0.0536× (z -10.3) |
| [[A-172 (line)]] | wt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.33× (z +13.7) | — |
| [[A549 (line)]] | wt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0807× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 6.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 5.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 8.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +8.7) | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.153× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 5.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +14.2) | — |
| [[RKO (line)]] | wt | 5.30 | 0 | 1 | — | [[Voriconazole (drug)]] 0.5 µM 0.0603× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 6.12 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0662× (z -9.5) |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.102× (z -9.0) |
| [[SW48 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +11.9) | — |
| [[SW480 (line)]] | alt | 13.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.9) | — |
| [[A498 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 167), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | +0.79 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[SRRM2]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SCAF1]] | +0.74 | +0.84 / +0.65 | both halves | 7e-06 |  |
| [[SRCAP]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[SRSF6]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.71 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[PIGO]] | +0.70 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[LINC00641]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[TFE3]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MMP25]] | +0.69 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[CIC]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.66 | +0.74 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF149]] | -0.66 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.65 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[NENF]] | -0.63 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[SNHG30]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[CCZ1B]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[CCZ1]] | -0.61 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[KLHDC10]] | -0.61 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.60 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[MALSU1]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[ASB7]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.60 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[NUP54]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF32-DT]] | B | RNF32-DT activity lowers CELSR3's level | lines that do not express RNF32-DT (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without RNF32-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: SPATA13; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.781). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.1, 4.0); signed map (15.2, -22.9). **Vector** length 88.9, 17.4% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +19.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +1.7 | +0.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | cadherin EGF LAG seven-pass G-type receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,636,463-48,662,886 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEGF2, HFMI1, FMI1, CDHF11, ADGRC3; previously EGFL1 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily C; CELSR cadherins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYQ7](https://www.uniprot.org/uniprotkb/Q9NYQ7) (Cadherin EGF LAG seven-pass G-type receptor 3):

> Receptor that may have an important role in cell/cell signaling during nervous system formation.

**Summary**, from NCBI Gene [1951](https://www.ncbi.nlm.nih.gov/gene/1951):

> This gene belongs to the flamingo subfamily, which is included in the cadherin superfamily. The flamingo cadherins consist of nonclassic-type cadherins that do not interact with catenins. They are plasma membrane proteins containing seven epidermal growth factor-like repeats, nine cadherin domains and two laminin A G-type repeats in their ectodomain. They also have seven transmembrane domains, a characteristic feature of their subfamily. The encoded protein may be involved in the regulation of …

**Accessions** — [HGNC:3230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3230) · Entrez [1951](https://www.ncbi.nlm.nih.gov/gene/1951) · UniProt [Q9NYQ7](https://www.uniprot.org/uniprotkb/Q9NYQ7) · Ensembl [ENSG00000008300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008300)

## Data

Gene col 167: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 167); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 167, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 167]; `tensor/DDL_lfc|DDL_z.npy` [167]; `embed/gene_vectors.npy` [167]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 167 or target_col == 167). Every well: [[CELSR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELSR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

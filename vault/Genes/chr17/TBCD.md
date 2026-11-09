---
symbol: "TBCD"
type: "gene"
col: 6544
ensembl_id: "ENSG00000141556"
name: "tubulin folding cofactor D"
location: "17q25.3"
module: 11
arm: "-"
pooled_cpm: 81.18
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TBCD

*tubulin folding cofactor D* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.00× (z +18.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.585× (z -8.6, q 7e-15, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF3]] (+0.73, fdr 7e-06), [[RPA1]] (+0.69, fdr 7e-06), [[WDR5]] (+0.69, fdr 7e-06); moves opposite to [[FAM200A]] (-0.72, fdr 7e-06), [[ZNF226]] (-0.68, fdr 1e-05), [[C14orf119]] (-0.68, fdr 1e-05).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC35G2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.00×** | +18.1 | 0e+00 | 46/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +16.1 | 0e+00 | 46/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.33×** | +13.9 | 9e-42 | 47/48 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +7.8 | 8e-13 | 41/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.45×** | +6.1 | 1e-07 | 35/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 3e-07 | 34/48 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.0 | 4e-05 | 37/49 (AsPC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | **1.27×** | +3.7 | 0.013 | 21/44 (LoVo, NCI-H1573, …) | rises with dose | composition shift |
| [[Budesonide (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.039 | 21/48 (LOX-IMVI, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | **1.23×** | +3.4 | 0.039 | 24/49 (LoVo, A498, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.075 | 16/49 (HepG2/C3A, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.44×** | +3.2 | 0.075 | 20/49 (SW48, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.585×** | -8.6 | 7e-15 | 38/48 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.795×** | -5.4 | 2e-05 | 25/48 (LS 180, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -5.2 | 4e-05 | 32/47 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 2e-04 | 26/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.817×** | -4.8 | 2e-04 | 25/48 (AN3 CA, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.009 | 24/48 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.8 | 0.013 | 21/49 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.873× | -3.2 | 0.095 | 13/48 (SW48, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.0 | 0.14 | 19/48 (C32, NCI-H661, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.880× | -3.0 | 0.14 | 9/49 (SNU-1, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 160 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.300× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 83.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.344× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 40.5 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.84× (z +12.4) | [[Harringtonine (drug)]] 5 µM 0.384× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 131 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.17× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.461× (z -8.7) |
| [[CHP-212 (line)]] | wt | 135 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.16× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.159× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 40.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 132 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.448× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 62.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.52× (z +14.6) | — |
| [[SW480 (line)]] | alt | 58.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.35× (z +19.7) | — |
| [[A-172 (line)]] | wt | 83.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -12.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.406× (z -9.0) |
| [[A498 (line)]] | wt | 41.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +13.6) | — |
| [[A549 (line)]] | wt | 73.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 20.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +11.4) | — |
| [[H4 (line)]] | wt | 54.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +10.2) | — |
| [[HOP62 (line)]] | alt | 81.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 46.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.45× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 74.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 57.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 46.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.01× (z +16.9) | — |
| [[Panc 03.27 (line)]] | alt | 71.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 44.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.22× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 64.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 44.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 49.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.07× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -21.2) ⚠ cell-cycle shift, explains ~80% of this change |
| [[C-33 A (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 35.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.232× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 50.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 60.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.61× (z +8.6) | — |
| [[KATO III (line)]] | alt | 152 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H23 (line)]] | alt | 98.6 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.32× (z +9.4) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.337× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 49.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.3) | — |
| [[RKO (line)]] | wt | 75.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.88× (z +9.2) | — |
| [[A-427 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -13.6) ⚠ cell-cycle shift, explains ~80% of this change |
| [[MIA PaCa-2 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 194 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF3]] | +0.73 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RPA1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[WDR5]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TRAF7]] | +0.68 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SETD3]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[DAZAP1]] | +0.65 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[GLB1L2]] | +0.65 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[POLD2]] | +0.65 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[TBC1D24]] | +0.64 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[CEP131]] | +0.64 | +0.50 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ABCA2]] | +0.64 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NPHP4]] | +0.63 | +0.63 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | -0.72 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[ZNF226]] | -0.68 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.68 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[ZNF181]] | -0.67 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[MED18]] | -0.67 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.66 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | -0.66 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[HELQ]] | -0.65 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF341-AS1]] | -0.64 | -0.60 / -0.37 | both halves | 7e-05 |  |
| [[PBDC1]] | -0.64 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TOPORS]] | -0.64 | -0.52 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35G2]] | B | SLC35G2 activity lowers TBCD's level | lines that do not express SLC35G2 (12) vs lines expressing it (38) | 1.56× higher at baseline in the lines without SLC35G2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: SMARCA1, LARP6, ZSCAN12 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.0, 6.2); signed map (-44.4, -12.4). **Vector** length 123, 36.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.4 | +18.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | +13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.3 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | +6.0 | +3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +6.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +0.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.6 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.9 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -7.4 | -4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.6 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | tubulin folding cofactor D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,752,042-82,945,914 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 2 pathways, smallest: Post-chaperonin tubulin folding pathway; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTW9](https://www.uniprot.org/uniprotkb/Q9BTW9) (Tubulin-specific chaperone D):

> Tubulin-folding protein implicated in the first step of the tubulin folding pathway and required for tubulin complex assembly. Involved in the regulation of microtubule polymerization or depolymerization, it modulates microtubule dynamics by capturing GTP-bound beta-tubulin (TUBB). Its ability to interact with beta tubulin is regulated via its interaction with ARL2. Acts as a GTPase-activating protein (GAP) for ARL2. Induces microtubule disruption in absence of ARL2. Increases degradation of …

**Summary**, from NCBI Gene [6904](https://www.ncbi.nlm.nih.gov/gene/6904):

> Cofactor D is one of four proteins (cofactors A, D, E, and C) involved in the pathway leading to correctly folded beta-tubulin from folding intermediates. Cofactors A and D are believed to play a role in capturing and stabilizing beta-tubulin intermediates in a quasi-native confirmation. Cofactor E binds to the cofactor D/beta-tubulin complex; interaction with cofactor C then causes the release of beta-tubulin polypeptides that are committed to the native state. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11581](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11581) · Entrez [6904](https://www.ncbi.nlm.nih.gov/gene/6904) · UniProt [Q9BTW9](https://www.uniprot.org/uniprotkb/Q9BTW9) · Ensembl [ENSG00000141556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141556)

## Data

Gene col 6544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6544); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6544]; `tensor/DDL_lfc|DDL_z.npy` [6544]; `embed/gene_vectors.npy` [6544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6544 or target_col == 6544). Every well: [[TBCD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBCD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

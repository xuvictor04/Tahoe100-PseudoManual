---
symbol: "TSPYL1"
type: "gene"
col: 12109
ensembl_id: "ENSG00000189241"
name: "TSPY like 1"
location: "6q22.1"
module: 7
arm: "+"
pooled_cpm: 25.68
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TSPYL1

*TSPY like 1* — 6q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +15.9, q 0e+00, up in 40 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0718×); [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.164×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF646]] (+0.64, fdr 7e-06), [[PAF1]] (+0.63, fdr 1e-05), [[EIF4G2]] (+0.63, fdr 1e-05); moves opposite to [[EIF3K]] (-0.59, fdr 2e-05), [[NAA35]] (-0.54, fdr 4e-05), [[UBE2Q2P2]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +15.9 | 0e+00 | 40/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +13.3 | 8e-38 | 44/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +8.7 | 5e-16 | 35/48 (HEC-1-A, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +8.6 | 2e-15 | 39/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +8.4 | 5e-15 | 37/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +8.3 | 8e-15 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.2 | 2e-14 | 32/47 (SNU-423, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +7.9 | 2e-13 | 37/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.8 | 3e-13 | 39/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +6.8 | 5e-10 | 29/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.3 | 1e-08 | 28/48 (PANC-1, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.3 | 1e-08 | 28/48 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 2e-08 | 34/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.46×** | +6.2 | 3e-08 | 26/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 8e-06 | 25/47 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +4.7 | 7e-05 | 24/48 (SW480, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ipatasertib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0718×); [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bergenin (drug)]] 0.5 µM |  | 0.800× | -3.7 | 0.15 | 17/48 (SW48, SW 900, …) | inconsistent across doses | position effect removed |
| [[Allantoin (drug)]] 0.5 µM |  | 0.828× | -3.1 | 0.56 | 12/48 (NCI-H460, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.4) | — |
| [[A549 (line)]] | wt | 13.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.2) | — |
| [[KATO III (line)]] | alt | 39.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 44.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 16.4 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.164× (z -10.5) |
| [[LoVo (line)]] | wt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0718× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.5) | — |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF646]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PAF1]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.63 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ZNF564]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DDX6]] | +0.61 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[VCPIP1]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SMCR8]] | +0.61 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[ZNF543]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MSANTD7]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[MED12]] | +0.60 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[IRF2BP1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[KLHL11]] | +0.59 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3K]] | -0.59 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NAA35]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[UBE2Q2P2]] | -0.51 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[RAC3]] | -0.51 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[TMEM120B]] | -0.51 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[EML2]] | -0.51 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[TOMM20]] | -0.50 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[L2HGDH]] | -0.50 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[SSBP4]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ETHE1]] | -0.49 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[LRRC75A]] | -0.49 | -0.21 / -0.50 | both halves | 6e-04 |  |
| [[TMEM160]] | -0.49 | -0.52 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TSPYL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF304]] | B | ZNF304 activity lowers TSPYL1's level | lines that do not express ZNF304 (10) vs lines expressing it (40) | 1.23× higher at baseline in the lines without ZNF304 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, ZNF256, RTL8C; its own permutation p |
| [[RAC3]] | B | RAC3 activity raises TSPYL1's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without RAC3 | 0.090 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.2, 14.1); signed map (5.2, -29.9). **Vector** length 76.8, 14.8% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.6 | +8.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | +4.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.1 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -0.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TSPY like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.1 — chr6:116,267,760-116,279,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously TSPYL |
| Gene groups (HGNC) | TSPYL family |
| Matched by | ensembl_id |

UniProt [Q9H0U9](https://www.uniprot.org/uniprotkb/Q9H0U9) carries no function annotation.

**Summary**, from NCBI Gene [7259](https://www.ncbi.nlm.nih.gov/gene/7259):

> The protein encoded by this gene is found in the nucleolus and is similar to that of a family of genes on the Y-chromosome. This gene is intronless. Defects in this gene are a cause of sudden infant death with dysgenesis of the testes syndrome (SIDDT). [provided by RefSeq, Dec 2009]

**Accessions** — [HGNC:12382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12382) · Entrez [7259](https://www.ncbi.nlm.nih.gov/gene/7259) · UniProt [Q9H0U9](https://www.uniprot.org/uniprotkb/Q9H0U9) · Ensembl [ENSG00000189241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189241)

## Data

Gene col 12109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12109); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12109]; `tensor/DDL_lfc|DDL_z.npy` [12109]; `embed/gene_vectors.npy` [12109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12109 or target_col == 12109). Every well: [[TSPYL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPYL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

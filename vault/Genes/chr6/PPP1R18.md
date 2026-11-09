---
symbol: "PPP1R18"
type: "gene"
col: 7066
ensembl_id: "ENSG00000146112"
name: "protein phosphatase 1 regulatory subunit 18"
location: "6p21.33"
module: 101
arm: "+"
pooled_cpm: 52.17
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# PPP1R18

*protein phosphatase 1 regulatory subunit 18* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.23× (z +10.1, q 2e-21, up in 32 of 43 measured lines) ⚠ position not correctable. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.57× (z +7.2, q 2e-10, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.480× (z -10.6, q 1e-23, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK10]] (+0.60, fdr 7e-06), [[FMNL3]] (+0.60, fdr 2e-05), [[ELF4]] (+0.58, fdr 1e-05); moves opposite to [[PHKA1]] (-0.48, fdr 9e-05), [[MSH3]] (-0.47, fdr 7e-05), [[IMMT]] (-0.47, fdr 2e-04).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[KLHL21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +10.1 | 2e-21 | 32/43 (J82, SNU-423, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +7.2 | 2e-10 | 32/44 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +6.5 | 2e-08 | 28/43 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +6.2 | 1e-07 | 30/43 (SW480, RKO, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.9 | 1e-04 | 24/41 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.5 | 0.041 | 15/43 (NCI-H1792, SW1417, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.3 | 0.083 | 19/41 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | 1.24× | +3.1 | 0.16 | 16/42 (NCI-H2030, C-33 A, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -10.6 | 1e-23 | 36/43 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.485×** | -10.5 | 2e-23 | 36/43 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.717×** | -4.8 | 3e-04 | 26/43 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.536×** | -4.7 | 3e-04 | 27/42 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.726×** | -4.7 | 4e-04 | 26/43 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.753×** | -4.0 | 0.007 | 24/42 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.764×** | -3.9 | 0.007 | 22/43 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.8 | 0.010 | 20/43 (RPMI-7951, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.629×** | -3.5 | 0.028 | 23/40 (Hs 766T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.789×** | -3.2 | 0.067 | 22/43 (hTERT-HPNE, LOX-IMVI, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.804×** | -3.2 | 0.079 | 20/43 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.808×** | -3.1 | 0.095 | 19/43 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 34.0 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +24.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 10.2× (z +20.3) | — |
| [[J82 (line)]] | alt | 122 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.33× (z +12.0) | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -10.6) |
| [[RPMI-7951 (line)]] | alt | 101 | 3 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.22× (z +10.7) | [[Tucidinostat (drug)]] 5 µM 0.523× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -11.6) |
| [[HS-578T (line)]] | alt | 123 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.40× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 57.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -11.8) |
| [[HOP62 (line)]] | alt | 72.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -13.2) |
| [[Hs 766T (line)]] | wt | 101 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.380× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 50.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.8) |
| [[A-172 (line)]] | wt | 87.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 71.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +10.3) ⚠ cell-cycle shift, explains ~89% of this change | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 42.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.27× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 140 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.424× (z -8.8) |
| [[SW1417 (line)]] | alt | 40.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.339× (z -9.2) |
| [[SW480 (line)]] | alt | 32.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +10.0) | — |
| [[A-427 (line)]] | wt | 11.1 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK10]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[FMNL3]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[ELF4]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GOLGA7B]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ZNF267]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[RIPOR1]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SYNGAP1]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[KDM6B]] | +0.54 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[NAB2]] | +0.54 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TRIM8]] | +0.54 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[PHLDB1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[GNL1]] | +0.53 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHKA1]] | -0.48 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[MSH3]] | -0.47 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[IMMT]] | -0.47 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[CDIN1]] | -0.46 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[VWA8]] | -0.46 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[LGR4]] | -0.45 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[PCCB]] | -0.44 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[UBR3]] | -0.44 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MRPL48]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[PTPN4]] | -0.44 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[CEP126]] | -0.44 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[DTWD2]] | -0.43 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL21]] | B | PPP1R18 activity raises KLHL21's level | lines that do not express PPP1R18 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without PPP1R18 | 0.017 | ⚠ within organs, on part of the lines; also absent: PER3, VIM-AS1, UPP1; maybe low, not absent |
| [[GABBR1]] | B | PPP1R18 activity raises GABBR1's level | lines that do not express PPP1R18 (5) vs lines expressing it (45) | 3.29× lower at baseline in the lines without PPP1R18 | 0.092 | ⚠ within organs, on part of the lines; also absent: PER3, VIM-AS1, UPP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, -2.2); signed map (2.4, 29.4). **Vector** length 106, 28.6% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.1 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +6.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +2.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.8 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[NG25 (drug)]] 5 µM |  | -4.1 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.4 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -1.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,676,389-30,687,895 (-) |
| Ensembl biotype | protein_coding |
| Also known as | phostensin; previously KIAA1949 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NYC8](https://www.uniprot.org/uniprotkb/Q6NYC8) (Phostensin):

> [Isoform 1]: May target protein phosphatase 1 to F-actin cytoskeleton.; [Isoform 4]: May target protein phosphatase 1 to F-actin cytoskeleton.

**Summary**, from NCBI Gene [170954](https://www.ncbi.nlm.nih.gov/gene/170954):

> Protein phosphatase-1 (PP1; see MIM 176875) interacts with regulatory subunits that target the enzyme to different cellular locations and change its activity toward specific substrates. Phostensin is a regulatory subunit that targets PP1 to F-actin (see MIM 102610) cytoskeleton (Kao et al., 2007 [PubMed 17374523]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29413](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29413) · Entrez [170954](https://www.ncbi.nlm.nih.gov/gene/170954) · UniProt [Q6NYC8](https://www.uniprot.org/uniprotkb/Q6NYC8) · Ensembl [ENSG00000146112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146112)

## Data

Gene col 7066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7066); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7066]; `tensor/DDL_lfc|DDL_z.npy` [7066]; `embed/gene_vectors.npy` [7066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7066 or target_col == 7066). Every well: [[PPP1R18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

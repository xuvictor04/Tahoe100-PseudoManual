---
symbol: "UBL4A"
type: "gene"
col: 2223
ensembl_id: "ENSG00000102178"
name: "ubiquitin like 4A"
location: "Xq28"
module: 33
arm: "+"
pooled_cpm: 9.96
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# UBL4A

*ubiquitin like 4A* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.66× (z +5.6, q 1e-05, up in 25 of 39 measured lines) ⚠ transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.60× (z +5.1, q 8e-05, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.500× (z -10.7, q 8e-24, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPTP]] (+0.68, fdr 7e-06), [[NSUN5]] (+0.66, fdr 1e-05), [[FADD]] (+0.63, fdr 1e-05); moves opposite to [[PRCP]] (-0.59, fdr 1e-05), [[GNAS]] (-0.58, fdr 4e-05), [[TMA7]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[C12orf73]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2223.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +5.6 | 1e-05 | 25/39 (HT-29, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.1 | 8e-05 | 25/46 (AsPC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.7 | 6e-04 | 23/46 (SW480, AsPC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.6 | 6e-04 | 10/18 (PANC-1, Hs 766T, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +4.5 | 6e-04 | 21/46 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 1.34× | +3.2 | 0.14 | 10/48 (SNU-423, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.500×** | -10.7 | 8e-24 | 30/43 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.533×** | -9.7 | 8e-20 | 34/44 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.503×** | -7.5 | 1e-11 | 32/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -6.7 | 4e-09 | 27/44 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -5.9 | 3e-07 | 22/45 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -5.8 | 7e-07 | 23/46 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -5.0 | 4e-05 | 22/45 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.684×** | -4.0 | 0.005 | 26/43 (SNU-423, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -3.9 | 0.005 | 22/45 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.708×** | -3.8 | 0.010 | 16/46 (J82, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.709×** | -3.5 | 0.028 | 15/46 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.747×** | -3.2 | 0.071 | 19/46 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -3.1 | 0.095 | 16/41 (BT-474, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.4) |
| [[MIA PaCa-2 (line)]] | alt | 9.98 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0894× (z -18.8) |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.9) |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.3) |
| [[J82 (line)]] | alt | 15.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 7.24 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -9.3) |
| [[A498 (line)]] | wt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.0) |
| [[A549 (line)]] | wt | 7.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 8.09 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -8.6) |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -9.8) |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -8.6) |
| [[KATO III (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -8.5) |
| [[RKO (line)]] | wt | 8.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0948× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 7.04 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0732× (z -9.5) |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.6) |
| [[SW480 (line)]] | alt | 10.00 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPTP]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[NSUN5]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[FADD]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MRPS2]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[RGS19]] | +0.63 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[NKRF]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RRP1B]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[RPP40]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[CBR1]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ASB6]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DCTPP1]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[RPUSD1]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCP]] | -0.59 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[GNAS]] | -0.58 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[TMA7]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[BCL2L14]] | -0.53 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TSPOAP1-AS1]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[HOXB-AS3]] | -0.53 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[FAM151B-DT]] | -0.53 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[OXR1-AS1]] | -0.52 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[EOGT-DT]] | -0.52 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[C12orf73]] | -0.52 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TMEM59]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ACADSB]] | -0.52 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBL4A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf73]] | C | UBL4A's natural level strengthens C12orf73's drug response | UBL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.14; direction not clear | 0.085 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Canagliflozin (drug)]] 5 µM | C | UBL4A's natural level lowers the cells' numbers under Canagliflozin 5 µM (makes them more sensitive) | UBL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.74 | 0.162 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | UBL4A's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | UBL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62 | 0.435 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | UBL4A's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | UBL4A's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.474 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.518). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.7, -1.7); signed map (-6.7, -28.2). **Vector** length 79.0, 15.7% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.4 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,483,717-154,486,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GDX, DXS254E, GET5, MDY2, TMA24; previously UBL4 |
| Gene groups (HGNC) | BAG6 complex; GET4-GET5 transmembrane domain recognition complex subunits |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P11441](https://www.uniprot.org/uniprotkb/P11441) (Ubiquitin-like protein 4A):

> As part of a cytosolic protein quality control complex, the BAG6/BAT3 complex, maintains misfolded and hydrophobic patches-containing proteins in a soluble state and participates in their proper delivery to the endoplasmic reticulum or alternatively can promote their sorting to the proteasome where they undergo degradation. The BAG6/BAT3 complex is involved in the post-translational delivery of tail-anchored/type II transmembrane proteins to the endoplasmic reticulum membrane. Recruited to …

**Summary**, from NCBI Gene [8266](https://www.ncbi.nlm.nih.gov/gene/8266):

> Enables protein-folding chaperone binding activity. Involved in several processes, including post-translational protein targeting to endoplasmic reticulum membrane; regulation of protein stability; and tail-anchored membrane protein insertion into ER membrane. Located in cytosol; membrane; and nucleoplasm. Part of BAT3 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12505) · Entrez [8266](https://www.ncbi.nlm.nih.gov/gene/8266) · UniProt [P11441](https://www.uniprot.org/uniprotkb/P11441) · Ensembl [ENSG00000102178](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102178)

## Data

Gene col 2223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2223); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2223]; `tensor/DDL_lfc|DDL_z.npy` [2223]; `embed/gene_vectors.npy` [2223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2223 or target_col == 2223). Every well: [[UBL4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBL4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

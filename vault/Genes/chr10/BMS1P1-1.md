---
symbol: "BMS1P1-1"
type: "gene"
col: 16565
ensembl_id: "ENSG00000291069"
name: ""
location: ""
module: 28
arm: "+"
pooled_cpm: 5.8
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 16
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# BMS1P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.42× (z +4.9, q 6e-04, up in 7 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.658× (z -8.3, q 9e-14, down in 22 of 40 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.589× (z -7.4, q 3e-11, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1P1]] (+0.81, fdr 7e-06, ⚠ same locus), [[AGAP13P]] (+0.72, fdr 7e-06, ⚠ same locus), [[AGAP9]] (+0.60, fdr 1e-05), [[SLC2A11]] (+0.58, fdr 3e-05), [[ZNF594-DT]] (+0.53, fdr 2e-05); moves opposite to [[HOOK3]] (-0.49, fdr 3e-05), [[PITRM1-AS1]] (-0.46, fdr 7e-05), [[MAPK8IP1]] (-0.46, fdr 3e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ECHDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 6e-04 | 7/46 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.039 | 5/35 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | 1.26× | +3.2 | 0.26 | 2/45 (KATO III, COLO 205) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.32 | 9/43 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.658×** | -8.3 | 9e-14 | 22/40 (AsPC-1, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.570×** | -7.9 | 1e-12 | 21/46 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -7.4 | 3e-11 | 23/44 (SW480, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.647×** | -5.8 | 7e-07 | 15/43 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -5.1 | 4e-05 | 13/45 (Panc 03.27, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.713×** | -4.7 | 2e-04 | 17/44 (KATO III, PANC-1, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -4.4 | 9e-04 | 13/47 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.749×** | -4.0 | 0.004 | 12/32 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -3.8 | 0.008 | 9/46 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.594×** | -3.8 | 0.008 | 7/43 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trimetrexate (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.012 | 7/43 (C32, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.777×** | -3.5 | 0.021 | 13/37 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.842× | -3.4 | 0.031 | 19/39 (J82, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.786×** | -3.4 | 0.032 | 12/27 (A549, PANC-1, …) | inconsistent across doses | composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **0.777×** | -3.3 | 0.042 | 7/43 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.651×** | -3.1 | 0.059 | 7/42 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -3.0 | 0.074 | 8/42 (PANC-1, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[A549 (line)]] | wt | 9.54 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[AsPC-1 (line)]] | alt | 5.80 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -12.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.0866× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[SW480 (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[HEC-1-A (line)]] | alt | 4.96 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0537× (z -13.3) |
| [[KATO III (line)]] | alt | 3.33 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.05 µM 0.0454× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 5.25 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW1417 (line)]] | alt | 4.89 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0587× (z -9.9) |
| [[A-172 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P1]] | +0.81 | +0.80 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP13P]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 | ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP9]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SLC2A11]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ZNF594-DT]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[LYRM9]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[NLRX1]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[PEX7]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ECHDC2]] | +0.51 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[TAB1]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MTHFS]] | +0.49 | +0.35 / +0.45 | both halves | 1e-04 |  |
| [[C5orf63]] | +0.49 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[ZNF839]] | +0.48 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ANGEL1]] | +0.48 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOOK3]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PITRM1-AS1]] | -0.46 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[MAPK8IP1]] | -0.46 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[HCN2]] | -0.45 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[TUBB3]] | -0.45 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[EPHA1-AS1]] | -0.44 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[CTNNA1]] | -0.43 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[C8orf88]] | -0.43 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[NBEAL1]] | -0.43 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[SLC6A8]] | -0.43 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CSRP2]] | -0.42 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[SNAI1]] | -0.42 | -0.37 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECHDC2]] | B | ECHDC2 activity raises BMS1P1-1's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.49× lower at baseline in the lines without ECHDC2 | 0.009 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[LIMCH1]] | B | LIMCH1 activity lowers BMS1P1-1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.34× higher at baseline in the lines without LIMCH1 | 0.097 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.209). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.4, 21.3); signed map (18.2, -44.7). **Vector** length 39.3, 3.76% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | -2.7 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.3 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | -2.2 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | -1.8 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -0.8 | -0.7 |

## What is on record

> [!warning] No registry record
> BMS1P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16565); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16565]; `tensor/DDL_lfc|DDL_z.npy` [16565]; `embed/gene_vectors.npy` [16565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16565 or target_col == 16565). Every well: [[BMS1P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "TMA7"
type: "gene"
col: 13837
ensembl_id: "ENSG00000232112"
name: "translation machinery associated 7 homolog"
location: "3p21.31"
module: 21
arm: "+"
pooled_cpm: 43.33
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TMA7

*translation machinery associated 7 homolog* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.81× (z +11.7, q 6e-29, up in 40 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +5.3, q 8e-06, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.721× (z -9.9, q 3e-20, down in 48 of 49 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 4 lines (NCI-H23 0.661×, J82 0.682×, HOP62 0.694×, NCI-H460 0.684×; ⚠ position not correctable).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL41]] (+0.70, fdr 1e-05), [[ATP5F1E]] (+0.60, fdr 7e-06), [[C12orf73]] (+0.57, fdr 1e-05); moves opposite to [[WDR18]] (-0.62, fdr 1e-05), [[PSMG1]] (-0.56, fdr 3e-05), [[DNAJB1]] (-0.56, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13837.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.81×** | +11.7 | 6e-29 | 40/40 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.30×** | +10.7 | 3e-24 | 46/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.92×** | +9.0 | 4e-17 | 44/44 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.30×** | +7.6 | 5e-12 | 45/46 (NCI-H460, SW480, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +6.4 | 1e-08 | 45/46 (NCI-H2030, RKO, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.3 | 8e-06 | 38/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.72×** | +5.0 | 6e-05 | 43/46 (HOP62, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.69×** | +4.8 | 1e-04 | 36/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.61×** | +4.2 | 0.002 | 33/48 (A-172, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.61×** | +4.2 | 0.002 | 33/47 (LS 180, LoVo, …) | top dose only |  |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.57×** | +4.2 | 0.002 | 40/48 (J82, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.53×** | +3.9 | 0.005 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mozavaptan (drug)]] 0.05 µM |  | **1.52×** | +3.5 | 0.017 | 33/47 (KATO III, HOP62, …) | inconsistent across doses | position effect removed |
| [[Gemcitabine (drug)]] 5 µM |  | **1.62×** | +3.2 | 0.044 | 33/48 (HCT15, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.98×** | +3.2 | 0.044 | 18/35 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13837.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 4 lines (NCI-H23 0.661×, J82 0.682×, HOP62 0.694×, NCI-H460 0.684×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.721×** | -9.9 | 3e-20 | 48/49 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.637×** | -3.6 | 0.078 | 34/48 (LS 180, NCI-H1573, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.678× | -3.1 | 0.33 | 27/48 (SK-MEL-2, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13837. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 43.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 56.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H460 (line)]] | wt | 32.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 48.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.67× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 73.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 54.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.48× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.19× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 36.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.51× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.33× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 39.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -9.2) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 79.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 37.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13837), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL41]] | +0.70 | +0.57 / +0.69 | both halves | 1e-05 | STRING 408 |
| [[ATP5F1E]] | +0.60 | +0.69 / +0.58 | both halves | 7e-06 | STRING 405 |
| [[C12orf73]] | +0.57 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[POMZP3]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[ZBTB47-AS1]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PABPN1]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[HOXB-AS3]] | +0.56 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | +0.54 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ANKRA2]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[EOGT-DT]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[UQCRB]] ⚠ | +0.53 | +0.61 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NDUFC1]] | +0.53 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR18]] | -0.62 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[DNAJB1]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[YDJC]] | -0.55 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[IFRD2]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[EIF6]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[UBL4A]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[DCTPP1]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[UBC]] | -0.52 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[GCLM]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[MSRB1]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RPUSD1]] | -0.51 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises TMA7's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.41× lower at baseline in the lines without SACS | 0.092 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.451). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.6, -42.8); signed map (39.1, -25.9). **Vector** length 58.1, 14.8% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +2.1 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.0 | +4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.8 |
|  | [[Ciclopirox (drug)]] 5 µM |  | +1.6 | +0.4 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.5 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.2 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | -0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | -2.3 | +4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -0.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | translation machinery associated 7 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,440,257-48,444,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC016; previously CCDC72 |
| Matched by | ensembl_id |

UniProt [Q9Y2S6](https://www.uniprot.org/uniprotkb/Q9Y2S6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26932](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26932) · Entrez [51372](https://www.ncbi.nlm.nih.gov/gene/51372) · UniProt [Q9Y2S6](https://www.uniprot.org/uniprotkb/Q9Y2S6) · Ensembl [ENSG00000232112](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232112)

## Data

Gene col 13837: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13837); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13837, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13837]; `tensor/DDL_lfc|DDL_z.npy` [13837]; `embed/gene_vectors.npy` [13837]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13837 or target_col == 13837). Every well: [[TMA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

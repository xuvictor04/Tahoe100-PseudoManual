---
symbol: "TUBA4A"
type: "gene"
col: 4833
ensembl_id: "ENSG00000127824"
name: "tubulin alpha 4a"
location: "2q35"
module: 60
arm: "+"
pooled_cpm: 13.02
n_lines_expressing: 37
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# TUBA4A

*tubulin alpha 4a* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +10.2, q 1e-21, up in 29 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.388× (z -4.1, q 0.025, down in 19 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB6]] (+0.63, fdr 1e-05, ⚠ same locus), [[BAG3]] (+0.62, fdr 1e-05), [[UBB]] (+0.59, fdr 1e-05), [[RELL2]] (+0.58, fdr 1e-05); moves opposite to [[DPY19L4]] (-0.56, fdr 5e-05), [[CPSF6]] (-0.54, fdr 1e-05), [[SF1]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RNF223]] → it (grade B ⚠); 10 go from it, the strongest it → [[KIAA1671]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +10.2 | 1e-21 | 29/34 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; position correction uncertain | **2.96×** | +9.3 | 3e-18 | 27/32 (SW1417, SW 900, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.93×** | +9.2 | 4e-18 | 35/35 (A-172, A498, …) | two highest doses |  |
| [[Docetaxel (drug)]] 5 µM | ⚠ position correction uncertain | **2.05×** | +8.7 | 4e-16 | 32/35 (NCI-H2030, NCI-H1792, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **2.64×** | +8.3 | 9e-15 | 30/34 (KATO III, LoVo, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **2.27×** | +7.1 | 2e-10 | 29/35 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.25×** | +7.0 | 3e-10 | 34/35 (A-172, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.23×** | +6.6 | 3e-09 | 23/31 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.4 | 1e-08 | 20/35 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.94×** | +5.7 | 7e-07 | 25/35 (NCI-H1792, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.93×** | +5.7 | 8e-07 | 24/35 (SK-MEL-2, LoVo, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.93×** | +5.6 | 8e-07 | 24/35 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ position correction uncertain | **2.04×** | +5.5 | 2e-06 | 26/34 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.94×** | +5.5 | 2e-06 | 23/31 (SW480, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.83×** | +5.2 | 9e-06 | 25/35 (LoVo, A549, …) | all doses, flat | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | **1.83×** | +5.0 | 2e-05 | 27/35 (LoVo, A549, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.87×** | +4.9 | 3e-05 | 24/33 (LoVo, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.007 | 15/35 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Triclosan (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.038 | 15/35 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.071 | 11/33 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4833.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (AsPC-1 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (AsPC-1 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.388×** | -4.1 | 0.025 | 19/34 (AsPC-1, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.698× | -3.1 | 0.44 | 18/34 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.61 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 25.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.1 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.09× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.07× (z +9.2) ⚠ transcription drop; position correction uncertain | — |
| [[SW480 (line)]] | alt | 24.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +10.4) | — |
| [[A498 (line)]] | wt | 21.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.14× (z +9.0) | — |
| [[A549 (line)]] | wt | 9.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.34× (z +8.6) | — |
| [[KATO III (line)]] | alt | 16.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.32× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.76× (z +11.7) | — |
| [[RKO (line)]] | wt | 9.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.0) | — |
| [[A-427 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB6]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | ⚠ same locus (30.7 kb, same strand: neighbours can correlate without regulation) |
| [[BAG3]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[UBB]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[RELL2]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[TM2D2]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[OSGIN1]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[PRAME]] | +0.53 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[SAMD8]] | +0.53 | +0.36 / +0.51 | both halves | 9e-05 |  |
| [[PLIN3]] | +0.53 | +0.22 / +0.66 | both halves | 6e-04 | pathway: Autophagy |
| [[C9orf24]] | +0.53 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[FAM219A]] | +0.53 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[MSX1]] | +0.52 | +0.36 / +0.56 | both halves | 9e-05 | pathway: HALLMARK_UV_RESPONSE_UP |
| [[CBR3]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | -0.56 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[CPSF6]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[SF1]] | -0.53 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[NUDT21]] | -0.53 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[VPS36]] | -0.52 | -0.33 / -0.63 | both halves | 1e-04 | pathway: HCMV Infection |
| [[NHLRC3]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ARPIN]] | -0.50 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[MANEA]] | -0.49 | -0.34 / -0.51 | both halves | 1e-04 | pathway: Asparagine N-linked glycosylation |
| [[NEK4]] | -0.49 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[SCAP]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MRPL42]] | -0.48 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[ENTPD5]] | -0.48 | -0.38 / -0.48 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF223]] | B | RNF223 activity raises TUBA4A's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 2.46× lower at baseline in the lines without RNF223 | 0.006 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[TOP2A]] | B | TOP2A activity lowers TUBA4A's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NMB]] | B | NMB activity raises TUBA4A's level | lines that do not express NMB (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without NMB | 0.060 | ⚠ within organs, on part of the lines; also absent: ENO2, ARFGEF3, STAT5A; maybe low, not absent; its own permutation p |
| [[PLEKHO1]] | B | PLEKHO1 activity lowers TUBA4A's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.13× higher at baseline in the lines without PLEKHO1 | 0.079 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[PTHLH]] | B | PTHLH activity raises TUBA4A's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 1.73× lower at baseline in the lines without PTHLH | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1671]] | B | TUBA4A activity raises KIAA1671's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without TUBA4A | 0.010 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[SPATS2]] | B | TUBA4A activity lowers SPATS2's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without TUBA4A | 0.021 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[TMEM237]] | B | TUBA4A activity lowers TMEM237's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without TUBA4A | 0.027 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[SH3YL1]] | B | TUBA4A activity raises SH3YL1's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.58× lower at baseline in the lines without TUBA4A | 0.033 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[SAR1B]] | B | TUBA4A activity raises SAR1B's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without TUBA4A | 0.038 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[POLD4]] | B | TUBA4A activity raises POLD4's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.74× lower at baseline in the lines without TUBA4A | 0.055 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[RNF223]] | B | TUBA4A activity raises RNF223's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 2.13× lower at baseline in the lines without TUBA4A | 0.056 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 5 µM | B | TUBA4A activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express TUBA4A (13) vs lines expressing it (35) | the lines without TUBA4A: 0.92× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| [[NMB]] | B | TUBA4A activity raises NMB's level | lines that do not express TUBA4A (13) vs lines expressing it (37) | 1.63× lower at baseline in the lines without TUBA4A | 0.094 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |
| cells under [[Irinotecan (drug)]] 0.5 µM | B | TUBA4A activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express TUBA4A (13) vs lines expressing it (35) | the lines without TUBA4A: 0.82× the cells of the other lines | 0.0999 | ⚠ within organs, on part of the lines; also absent: TNK1, ETV7, CDCP1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.360). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.2, -9.6); signed map (-40.3, 30.9). **Vector** length 75.5, 18.1% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ position correction uncertain | +4.0 | +5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -1.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.3 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | tubulin alpha 4a |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,249,710-219,277,902 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30169, H2-ALPHA; previously TUBA1 |
| Gene groups (HGNC) | Tubulin alpha family |
| Hallmark sets | UV_RESPONSE_UP, MTORC1_SIGNALING, MITOTIC_SPINDLE |
| Reactome | 93 pathways, smallest: Microtubule-dependent trafficking of connexons from Golgi to the plasma membrane; Transport of connexons to the plasma membrane; Gap junction assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P68366](https://www.uniprot.org/uniprotkb/P68366) (Tubulin alpha-4A chain):

> Tubulin is the major constituent of microtubules, a cylinder consisting of laterally associated linear protofilaments composed of alpha- and beta-tubulin heterodimers. Microtubules grow by the addition of GTP-tubulin dimers to the microtubule end, where a stabilizing cap forms. Below the cap, tubulin dimers are in GDP-bound state, owing to GTPase activity of alpha-tubulin.

**Summary**, from NCBI Gene [7277](https://www.ncbi.nlm.nih.gov/gene/7277):

> Microtubules of the eukaryotic cytoskeleton perform essential and diverse functions and are composed of a heterodimer of alpha and beta tubulin. The genes encoding these microtubule constituents are part of the tubulin superfamily, which is composed of six distinct families. Genes from the alpha, beta and gamma tubulin families are found in all eukaryotes. The alpha and beta tubulins represent the major components of microtubules, while gamma tubulin plays a critical role in the nucleation of …

**Accessions** — [HGNC:12407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12407) · Entrez [7277](https://www.ncbi.nlm.nih.gov/gene/7277) · UniProt [P68366](https://www.uniprot.org/uniprotkb/P68366) · Ensembl [ENSG00000127824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127824)

## Data

Gene col 4833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4833); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4833]; `tensor/DDL_lfc|DDL_z.npy` [4833]; `embed/gene_vectors.npy` [4833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4833 or target_col == 4833). Every well: [[TUBA4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBA4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

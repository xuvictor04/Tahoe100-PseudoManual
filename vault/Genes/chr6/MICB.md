---
symbol: "MICB"
type: "gene"
col: 12880
ensembl_id: "ENSG00000204516"
name: "MHC class I polypeptide-related sequence B"
location: "6p21.33"
module: 72
arm: "+"
pooled_cpm: 10.15
n_lines_expressing: 37
n_dd_up: 44
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# MICB

*MHC class I polypeptide-related sequence B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (19 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.90× (z +26.2, q 0e+00, up in 32 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0573×; ⚠ cell-cycle shift, explains ~72% of this change); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (A549 0.0617×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MICA]] (+0.58, fdr 4e-05), [[HSPE1-MOB4]] (+0.58, fdr 2e-05), [[PI4K2B]] (+0.56, fdr 2e-05); moves opposite to [[EIF2B3]] (-0.52, fdr 6e-05), [[FAR2P1]] (-0.51, fdr 2e-04), [[MTRES1]] (-0.51, fdr 3e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF738]] → it (grade B ⚠); 7 go from it, the strongest it → [[AGK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.90×** | +26.2 | 0e+00 | 32/33 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.28×** | +13.9 | 3e-41 | 32/34 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.08×** | +12.4 | 4e-33 | 32/34 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.80×** | +12.0 | 4e-31 | 28/34 (Panc 03.27, J82, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.67×** | +11.5 | 2e-28 | 30/34 (A498, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.76×** | +11.4 | 4e-28 | 27/32 (NCI-H2030, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.63×** | +11.3 | 1e-27 | 26/34 (Panc 03.27, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.61×** | +11.2 | 2e-27 | 28/34 (SNU-423, J82, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.60×** | +10.7 | 4e-25 | 30/31 (A498, NCI-H2030, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.25×** | +10.1 | 2e-22 | 20/20 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +9.6 | 5e-20 | 29/34 (A-427, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.3 | 4e-15 | 25/35 (J82, HOP62, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.58×** | +7.9 | 1e-13 | 26/34 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +7.9 | 1e-13 | 17/35 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.00×** | +7.8 | 2e-13 | 22/30 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +7.8 | 3e-13 | 19/32 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.77×** | +6.7 | 6e-10 | 17/33 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.3 | 2e-06 | 10/34 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.3 | 3e-06 | 14/35 (A498, HOP62, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.35×** | +5.2 | 4e-06 | 15/32 (A498, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 1e-04 | 14/35 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.001 | 7/34 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12880.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0573×; ⚠ cell-cycle shift, explains ~72% of this change); [[Cabozantinib (S-malate) (drug)]] 0.5 µM in 1 line (A549 0.0617×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW1417 0.159×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.751× | -3.3 | 0.27 | 8/34 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.819× | -3.3 | 0.27 | 11/34 (Panc 03.27, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.75× (z +12.9) | — |
| [[J82 (line)]] | alt | 24.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +13.3) | — |
| [[A-172 (line)]] | wt | 11.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +9.8) | — |
| [[A-427 (line)]] | wt | 38.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.21× (z +9.1) | — |
| [[A549 (line)]] | wt | 2.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.50× (z +9.9) | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0617× (z -9.1) |
| [[LoVo (line)]] | wt | 6.42 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 4.89 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 36.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 16.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +12.4) | — |
| [[C32 (line)]] | wt | 4.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.83× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 8.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.75× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 3.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.19× (z +19.9) | — |
| [[NCI-H23 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0573× (z -10.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW1417 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 8.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.626 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICA]] | +0.58 | +0.41 / +0.64 | both halves | 4e-05 | same gene group; pathway: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; STRING 918 |
| [[HSPE1-MOB4]] | +0.58 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[PI4K2B]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[DEDD2]] | +0.55 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[MLLT11]] | +0.55 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[ALKBH6]] | +0.54 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[CDH24]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PDCL]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[MRPL18]] | +0.53 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ABHD17B]] | +0.52 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[PSMB4]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[MBOAT7]] | +0.51 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B3]] | -0.52 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[FAR2P1]] | -0.51 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[MTRES1]] | -0.51 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[TAMM41]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[DDX18]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[FARSB]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[UTP14A]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.49 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[DDX10]] | -0.49 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[MECR]] | -0.49 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[TXNRD3]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CEP63]] | -0.48 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF738]] | B | ZNF738 activity raises MICB's level | lines that do not express ZNF738 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without ZNF738 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF493, ENSG00000269237, ZNF66 |
| [[TOP2A]] | B | TOP2A activity lowers MICB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TXNRD3]] | C | TXNRD3 activity raises MICB's level | lines that do not express TXNRD3 (3) vs lines expressing it (47) | 4.06× lower at baseline in the lines without TXNRD3 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FSCN1, ELK3, XG |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGK]] | B | MICB activity raises AGK's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without MICB | 0.022 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[RAD9A]] | B | MICB activity lowers RAD9A's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.71× higher at baseline in the lines without MICB | 0.025 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[RHEBL1]] | B | MICB activity raises RHEBL1's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without MICB | 0.028 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[TTC26]] | B | MICB activity raises TTC26's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without MICB | 0.093 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[TXNRD3]] | B | MICB activity raises TXNRD3's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without MICB | 0.094 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[MICA]] | B | MICB activity raises MICA's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without MICB | 0.095 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[WDR35]] | B | MICB activity raises WDR35's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without MICB | 0.098 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.1, -7.0); signed map (-22.3, -28.2). **Vector** length 71.8, 15.6% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +26.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.6 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +12.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +8.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +7.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +4.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.2 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | MHC class I polypeptide-related sequence B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,494,881-31,511,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PERB11.2 |
| Gene groups (HGNC) | C1-set domain containing; MIC family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q29980](https://www.uniprot.org/uniprotkb/Q29980) (MHC class I polypeptide-related sequence B):

> Widely expressed membrane-bound protein which acts as a ligand to stimulate an activating receptor KLRK1/NKG2D, expressed on the surface of essentially all human natural killer (NK), gammadelta T and CD8+ alphabeta T-cells. Up-regulated in stressed conditions, such as viral and bacterial infections or DNA damage response, serves as signal of cellular stress, and engagement of KLRK1/NKG2D by MICA triggers NK-cells resulting in a range of immune effector functions, such as cytotoxicity and …

**Summary**, from NCBI Gene [4277](https://www.ncbi.nlm.nih.gov/gene/4277):

> This gene encodes a heavily glycosylated protein which is a ligand for the NKG2D type II receptor. Binding of the ligand activates the cytolytic response of natural killer (NK) cells, CD8 alphabeta T cells, and gammadelta T cells which express the receptor. This protein is stress-induced and is similar to MHC class I molecules; however, it does not associate with beta-2-microglobulin or bind peptides. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

**Accessions** — [HGNC:7091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7091) · Entrez [4277](https://www.ncbi.nlm.nih.gov/gene/4277) · UniProt [Q29980](https://www.uniprot.org/uniprotkb/Q29980) · Ensembl [ENSG00000204516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204516)

## Data

Gene col 12880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12880); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12880]; `tensor/DDL_lfc|DDL_z.npy` [12880]; `embed/gene_vectors.npy` [12880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12880 or target_col == 12880). Every well: [[MICB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "VAT1L"
type: "gene"
col: 10153
ensembl_id: "ENSG00000171724"
name: "vesicle amine transport 1 like"
location: "16q23.1"
module: 61
arm: "+"
pooled_cpm: 2.79
n_lines_expressing: 27
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# VAT1L

*vesicle amine transport 1 like* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.31× (z +22.2, q 0e+00, up in 19 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.607× (z -4.4, q 0.007, down in 2 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HOP62 0.0415×, A-427 0.168×, SW 900 0.0683×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SW 900 0.0324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.162×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.184×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.0578×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.153×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NTNG2]] (+0.68, fdr 7e-06), [[COLEC12]] (+0.67, fdr 2e-05), [[SYN1]] (+0.66, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PKIA]] → it (grade B ⚠); 9 go from it, the strongest it → [[RASA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.31×** | +22.2 | 0e+00 | 19/20 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.82×** | +14.2 | 3e-43 | 2/6 (RPMI-7951, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.62×** | +12.1 | 3e-31 | 16/18 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.24×** | +11.0 | 4e-26 | 5/8 (RPMI-7951, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +10.2 | 2e-22 | 2/6 (RPMI-7951, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +10.0 | 1e-21 | 6/17 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +8.8 | 1e-16 | 19/21 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +7.8 | 6e-13 | 18/21 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +7.7 | 8e-13 | 17/21 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.18×** | +7.3 | 2e-11 | 17/21 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.72×** | +4.9 | 5e-05 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.4 | 6e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.51×** | +3.8 | 0.006 | 1/15 (NCI-H460) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +3.5 | 0.017 | 13/18 (RPMI-7951, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.022 | 3/13 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.48×** | +3.4 | 0.022 | 0/13 | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.034 | 1/16 (NCI-H1792) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.037 | 5/15 (RPMI-7951, SW 900, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Sulfisoxazole (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.045 | 3/19 (C32, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10153.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (HOP62 0.0415×, A-427 0.168×, SW 900 0.0683×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (SW 900 0.0324×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 0.162×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-427 0.184×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.0578×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.607×** | -4.4 | 0.007 | 2/21 (HOP62, SW 900) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -3.6 | 0.091 | 7/22 (A-427, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.704× | -3.3 | 0.17 | 1/20 (NCI-H2030) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.726× | -3.0 | 0.28 | 6/19 (A549, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.726× | -3.0 | 0.28 | 5/18 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 34.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.184× (z -10.0) |
| [[HOP62 (line)]] | alt | 6.93 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 8.24× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0415× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Adagrasib (drug)]] 0.5 µM 0.0901× (z -8.5) |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0324× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0578× (z -9.7) |
| [[SW480 (line)]] | alt | 2.08 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 65.0× (z +18.3) | — |
| [[A-172 (line)]] | wt | 3.32 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.9× (z +11.0) | — |
| [[A549 (line)]] | wt | 0.939 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 48.3× (z +10.8) | — |
| [[H4 (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 2.24 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 1.19 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 19.1× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.9× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 4.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.01× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 0.972 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 27.0× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.42× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 4.09 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.3× (z +9.3) | — |
| [[A498 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.713 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.565 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.599 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.531 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.554 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.701 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.640 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.625 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTNG2]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[COLEC12]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[SYN1]] | +0.66 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[EPHB1]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[COL5A3]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[IL11]] | +0.64 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[CACNG7]] | +0.63 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[ITGA11]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[CSMD2]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.63 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[RAC2]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ALK]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIA]] | B | PKIA activity raises VAT1L's level | lines that do not express PKIA (22) vs lines expressing it (28) | 2.11× lower at baseline in the lines without PKIA | 0.047 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[LINC02813]] | B | LINC02813 activity raises VAT1L's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.06× lower at baseline in the lines without LINC02813 | 0.059 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[CSMD2]] | C | CSMD2 activity raises VAT1L's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without CSMD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[PLEKHG4B]] | C | PLEKHG4B activity raises VAT1L's level | lines that do not express PLEKHG4B (27) vs lines expressing it (23) | 2.66× lower at baseline in the lines without PLEKHG4B | 0.040 | ⚠ within organs, on part of the lines; also absent: CHST8, SNAP91, JAKMIP1; co-absent with the target |
| [[NDNF]] | C | NDNF activity raises VAT1L's level | lines that do not express NDNF (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without NDNF | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAM23, GUCY1B1, CNRIP1; co-absent with the target |
| [[ADAMTS18]] | C | ADAMTS18 activity raises VAT1L's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without ADAMTS18 | 0.083 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises VAT1L's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without NTNG2 | 0.086 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | VAT1L activity raises RASA3's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 1.18× lower at baseline in the lines without VAT1L | 0.040 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[HEYL]] | B | VAT1L activity raises HEYL's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 1.68× lower at baseline in the lines without VAT1L | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[ALK]] | B | VAT1L activity raises ALK's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without VAT1L | 0.064 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[CRMP1]] | C | VAT1L activity raises CRMP1's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 3.17× lower at baseline in the lines without VAT1L | 0.007 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[TSHZ3]] | C | VAT1L activity raises TSHZ3's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 5.11× lower at baseline in the lines without VAT1L | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[TRIM9]] | C | VAT1L activity raises TRIM9's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 4.49× lower at baseline in the lines without VAT1L | 0.028 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[ADAMTS18]] | C | VAT1L activity raises ADAMTS18's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without VAT1L | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[RUNX3]] | C | VAT1L activity raises RUNX3's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 4.31× lower at baseline in the lines without VAT1L | 0.039 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |
| [[NTNG2]] | C | VAT1L activity raises NTNG2's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 2.17× lower at baseline in the lines without VAT1L | 0.043 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.0, 13.8); signed map (31.7, 26.2). **Vector** length 55.1, 13.8% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +22.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +1.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | vesicle amine transport 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:77,788,564-77,980,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1576 |
| Gene groups (HGNC) | Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCJ6](https://www.uniprot.org/uniprotkb/Q9HCJ6) (Putative NADPH-dependent quinone oxidoreductase VAT1L):

> Putative NADPH-dependent quinone oxidoreductase.

**Summary**, from NCBI Gene [57687](https://www.ncbi.nlm.nih.gov/gene/57687):

> Predicted to enable NADPH dehydrogenase (quinone) activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29315) · Entrez [57687](https://www.ncbi.nlm.nih.gov/gene/57687) · UniProt [Q9HCJ6](https://www.uniprot.org/uniprotkb/Q9HCJ6) · Ensembl [ENSG00000171724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171724)

## Data

Gene col 10153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10153); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10153]; `tensor/DDL_lfc|DDL_z.npy` [10153]; `embed/gene_vectors.npy` [10153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10153 or target_col == 10153). Every well: [[VAT1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAT1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

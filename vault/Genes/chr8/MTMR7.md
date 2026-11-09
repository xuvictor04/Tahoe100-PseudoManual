---
symbol: "MTMR7"
type: "gene"
col: 38
ensembl_id: "ENSG00000003987"
name: "myotubularin related protein 7"
location: "8p22"
module: 9
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 34
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 12
direction_downstream: 17
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MTMR7

*myotubularin related protein 7* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +9.6, q 6e-19, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +9.0, q 4e-17, up in 11 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.626× (z -4.5, q 0.003, down in 10 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.222×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.247×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.212×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC7A2]] (+0.77, fdr 7e-06), [[CDH10]] (+0.63, fdr 1e-05), [[NELL1]] (+0.62, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 17 go from it, the strongest it → cells under [[Gemcitabine (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 38.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +9.6 | 6e-19 | 3/7 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.0 | 4e-17 | 11/21 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +7.9 | 6e-13 | 1/3 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +6.6 | 6e-09 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +6.6 | 6e-09 | 1/8 (NCI-H23) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.8 | 2e-04 | 7/21 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +4.8 | 2e-04 | 7/28 (NCI-H23, NCI-H1792, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.4 | 9e-04 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.011 | 3/18 (LOX-IMVI, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.024 | 2/17 (NCI-H1792, HepG2/C3A) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.5 | 0.025 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.5 | 0.025 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.036 | 2/14 (HEC-1-A, SW480) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.038 | 1/28 (HEC-1-A) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.047 | 1/15 (HOP62) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.052 | 5/28 (H4, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.073 | 7/26 (H4, HS-578T, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.095 | 4/28 (HS-578T, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 38.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.222×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.247×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.626×** | -4.5 | 0.003 | 10/25 (HepG2/C3A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.636×** | -4.4 | 0.003 | 5/27 (HS-578T, NCI-H23, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | 0.722× | -3.2 | 0.31 | 3/27 (HOP62, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 38. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 245 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.222× (z -9.8) |
| [[A-427 (line)]] | wt | 32.9 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -8.8) |
| [[HS-578T (line)]] | alt | 4.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +9.0) | — |
| [[A-172 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 38), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC7A2]] | +0.77 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CDH10]] | +0.63 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NELL1]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[KCNJ6]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADGRL3]] | +0.60 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[KCNG2]] | +0.60 | +0.63 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[KCNMB2]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RAB3C]] | +0.58 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PPFIA2]] | +0.58 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[GRIK1]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[LINC02197]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises MTMR7's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.95× lower at baseline in the lines without CALCA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[RIT2]] | B | RIT2 activity raises MTMR7's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 4.14× lower at baseline in the lines without RIT2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[TOP2A]] | B | TOP2A activity lowers MTMR7's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LIN7A]] | B | LIN7A activity raises MTMR7's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without LIN7A | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1 |
| [[BCHE]] | B | BCHE activity raises MTMR7's level | lines that do not express BCHE (35) vs lines expressing it (15) | 2.45× lower at baseline in the lines without BCHE | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2 |
| [[SYT4]] | B | SYT4 activity raises MTMR7's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.91× lower at baseline in the lines without SYT4 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[LINC02197]] | B | LINC02197 activity raises MTMR7's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.02× lower at baseline in the lines without LINC02197 | 0.059 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent |
| [[SLC7A2]] | B | SLC7A2 activity raises MTMR7's level | lines that do not express SLC7A2 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without SLC7A2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, HGF, UNC5D |
| [[H19]] | B | H19 activity raises MTMR7's level | lines that do not express H19 (38) vs lines expressing it (12) | 1.63× lower at baseline in the lines without H19 | 0.088 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA |
| [[KCNH5]] | B | KCNH5 activity raises MTMR7's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.47× lower at baseline in the lines without KCNH5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D |
| [[PCSK1]] | B | PCSK1 activity raises MTMR7's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 2.29× lower at baseline in the lines without PCSK1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[ASCL1]] | B | ASCL1 activity raises MTMR7's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 2.36× lower at baseline in the lines without ASCL1 | 0.0999 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Gemcitabine (drug)]] 5 µM | B | MTMR7 activity lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.19× the cells of the other lines | 0.022 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[TMTC1]] | B | MTMR7 activity raises TMTC1's level | lines that do not express MTMR7 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without MTMR7 | 0.024 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[ML264 (drug)]] 5 µM | B | MTMR7 activity raises the cells' numbers under ML264 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.78× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Raltitrexed (drug)]] 0.5 µM | B | MTMR7 activity raises the cells' numbers under Raltitrexed 0.5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.82× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Dabrafenib (drug)]] 5 µM | B | MTMR7 activity raises the cells' numbers under Dabrafenib 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.80× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM | B | MTMR7 activity raises the cells' numbers under Pyridoxine (hydrochloride) 0.5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.86× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Pyridoxine (hydrochloride) (drug)]] 5 µM | B | MTMR7 activity raises the cells' numbers under Pyridoxine (hydrochloride) 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.87× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[PF-06260933 (drug)]] 5 µM | B | MTMR7 activity raises the cells' numbers under PF-06260933 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.77× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[BCHE]] | B | MTMR7 activity raises BCHE's level | lines that do not express MTMR7 (16) vs lines expressing it (34) | 3.60× lower at baseline in the lines without MTMR7 | 0.052 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Allantoin (drug)]] 0.5 µM | B | MTMR7 activity lowers the cells' numbers under Allantoin 0.5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.15× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[NG25 (drug)]] 5 µM | B | MTMR7 activity lowers the cells' numbers under NG25 5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.40× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| cells under [[Medroxyprogesterone acetate (drug)]] 0.5 µM | B | MTMR7 activity lowers the cells' numbers under Medroxyprogesterone acetate 0.5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.28× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.1, 34.2); signed map (41.9, 35.4). **Vector** length 39.0, 6.15% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,296,794-17,413,528 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Myotubularins; Phosphoinositide phosphatases |
| Reactome | 6 pathways, smallest: Synthesis of PIPs at the late endosome membrane; Synthesis of IP2, IP, and Ins in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y216](https://www.uniprot.org/uniprotkb/Q9Y216) (Phosphatidylinositol-3-phosphate phosphatase MTMR7):

> Lipid phosphatase that specifically dephosphorylates the D-3 position of phosphatidylinositol 3-phosphate (PtdIns(3)P) and inositol 1,3-bisphosphate (Ins(1,3)P2).

**Summary**, from NCBI Gene [9108](https://www.ncbi.nlm.nih.gov/gene/9108):

> This gene encodes a member of the myotubularin family of tyrosine/dual-specificity phosphatases. The encoded protein is characterized by four distinct domains that are conserved among all members of the myotubularin family: the glucosyltransferase, Rab-like GTPase activator and myotubularins domain, the Rac-induced recruitment domain, the protein tyrosine phosphatases and dual-specificity phosphatases domain and the suppressor of variegation 3-9, enhancer-of-zeste, and trithorax interaction …

**Accessions** — [HGNC:7454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7454) · Entrez [9108](https://www.ncbi.nlm.nih.gov/gene/9108) · UniProt [Q9Y216](https://www.uniprot.org/uniprotkb/Q9Y216) · Ensembl [ENSG00000003987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003987)

## Data

Gene col 38: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 38); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 38, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 38]; `tensor/DDL_lfc|DDL_z.npy` [38]; `embed/gene_vectors.npy` [38]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 38 or target_col == 38). Every well: [[MTMR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

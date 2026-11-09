---
symbol: "CFAP70"
type: "gene"
col: 7943
ensembl_id: "ENSG00000156042"
name: "cilia and flagella associated protein 70"
location: "10q22.2"
module: 39
arm: "+"
pooled_cpm: 12.82
n_lines_expressing: 48
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 27
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# CFAP70

*cilia and flagella associated protein 70* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.15× (z +19.8, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.582× (z -4.6, q 0.002, down in 24 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.221×, A-427 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.129×, KATO III 0.310×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (H4 0.0462×, KATO III 0.324×); [[Ligustrazine (drug)]] 0.05 µM in 1 line (A-172 0.0680×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B3]] (+0.82, fdr 7e-06), [[NQO1-DT]] (+0.81, fdr 7e-06), [[NEB]] (+0.81, fdr 7e-06); moves opposite to [[BRAT1]] (-0.70, fdr 4e-05), [[L2HGDH]] (-0.70, fdr 4e-05), [[SDHAF3]] (-0.67, fdr 8e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ST8SIA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.15×** | +19.8 | 0e+00 | 40/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +13.6 | 7e-40 | 39/43 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.37×** | +12.6 | 4e-34 | 36/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.23×** | +10.0 | 2e-21 | 41/45 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.15×** | +9.4 | 4e-19 | 36/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +8.8 | 1e-16 | 35/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.00×** | +8.4 | 4e-15 | 37/46 (A-172, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +7.2 | 4e-11 | 34/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +6.6 | 2e-09 | 14/28 (SNU-423, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +6.3 | 1e-08 | 12/23 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +6.1 | 5e-08 | 29/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +5.6 | 1e-06 | 32/45 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.92×** | +5.6 | 1e-06 | 27/45 (HCT15, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +5.4 | 2e-06 | 17/35 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.91×** | +5.2 | 7e-06 | 25/42 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +4.8 | 7e-05 | 23/45 (COLO 205, NCI-H1573, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +4.7 | 7e-05 | 21/43 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.74×** | +4.7 | 7e-05 | 23/45 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.221×, A-427 0.234×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.129×, KATO III 0.310×); [[Digitoxin (drug)]] 0.5 µM in 2 lines (H4 0.0462×, KATO III 0.324×); [[Ligustrazine (drug)]] 0.05 µM in 1 line (A-172 0.0680×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -4.6 | 0.002 | 24/45 (H4, KATO III, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.371×** | -4.4 | 0.002 | 22/39 (KATO III, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -3.6 | 0.050 | 19/44 (NCI-H1573, KATO III, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.662× | -3.1 | 0.22 | 17/44 (NCI-H2030, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | 0.501× | -3.1 | 0.22 | 16/44 (KATO III, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 70.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.310× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 8.90 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +18.9) | — |
| [[SW480 (line)]] | alt | 14.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.3) | — |
| [[A-172 (line)]] | wt | 9.04 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.1) | [[Ligustrazine (drug)]] 0.05 µM 0.0680× (z -9.9) |
| [[HCT15 (line)]] | alt | 44.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -9.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 5.04 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.93× (z +9.3) | [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM 0.0694× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 19.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -10.9) |
| [[LoVo (line)]] | wt | 14.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +17.9) | — |
| [[HepG2_C3A (line)]] | wt | 33.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +9.2) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0729× (z -11.4) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 4.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +15.7) | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +8.9) | [[Rosiglitazone (drug)]] 5 µM 0.0738× (z -9.3) |
| [[A-427 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C32 (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.107× (z -8.5) ⚠ transcription drop |
| [[H4 (line)]] | wt | 20.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0462× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 27.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 8.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.02× (z +13.6) | — |
| [[HS-578T (line)]] | alt | 6.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.97× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 7.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 9.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 7.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +9.6) | — |
| [[RKO (line)]] | wt | 11.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0751× (z -8.8) |
| [[SNU-423 (line)]] | alt | 9.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +9.6) | — |
| [[SW48 (line)]] | wt | 9.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +11.0) | — |
| [[A498 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B3]] | +0.82 | +0.82 / +0.71 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.81 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[NEB]] | +0.81 | +0.86 / +0.64 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.81 | +0.83 / +0.65 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.79 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.79 | +0.83 / +0.63 | both halves | 7e-06 | STRING 720 |
| [[SLC6A13]] | +0.78 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[NEK11]] | +0.78 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.77 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[YIPF7]] | +0.77 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.82 / +0.56 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.76 | +0.75 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.70 | -0.67 / -0.40 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.70 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[SDHAF3]] | -0.67 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[FAM118A]] | -0.67 | -0.69 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST8SIA5]] | B | ST8SIA5 activity raises CFAP70's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 2.11× lower at baseline in the lines without ST8SIA5 | 0.034 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises CFAP70's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without FSIP2-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CFAP70's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AGA-DT]] | B | AGA-DT activity raises CFAP70's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without AGA-DT | 0.048 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[THBS4-AS1]] | B | THBS4-AS1 activity raises CFAP70's level | lines that do not express THBS4-AS1 (6) vs lines expressing it (44) | 2.00× lower at baseline in the lines without THBS4-AS1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.6, -11.8); signed map (20.9, 4.1). **Vector** length 95.8, 23.4% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.5 | +19.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.2 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +3.3 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | +4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | +4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | +8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.4 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +1.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,253,762-73,358,864 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25765; previously TTC18 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Cilia and flagella associated |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0N1](https://www.uniprot.org/uniprotkb/Q5T0N1) (Cilia- and flagella-associated protein 70):

> Axoneme-binding protein that plays a role in the regulation of ciliary motility and cilium length. Essential for the assembly of the sperm flagellum and the correct shaping of the sperm head, during spermiogenesis.Contributes in part to flagellar biogenesis by stabilizing QRICH2, promoting the cytoplasmic preassembly of CFAP61 and CFAP91, and regulating the manchette localization of axoneme-associated proteins such as IFT88, DNAI1 and CFAP61.

**Summary**, from NCBI Gene [118491](https://www.ncbi.nlm.nih.gov/gene/118491):

> Predicted to be involved in cilium assembly and cilium movement. Predicted to act upstream of or within several processes, including maintenance of cell number; single fertilization; and spermatid development. Located in ciliary basal body and sperm flagellum. Part of outer dynein arm. Implicated in spermatogenic failure 41. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30726) · Entrez [118491](https://www.ncbi.nlm.nih.gov/gene/118491) · UniProt [Q5T0N1](https://www.uniprot.org/uniprotkb/Q5T0N1) · Ensembl [ENSG00000156042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156042)

## Data

Gene col 7943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7943); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7943]; `tensor/DDL_lfc|DDL_z.npy` [7943]; `embed/gene_vectors.npy` [7943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7943 or target_col == 7943). Every well: [[CFAP70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

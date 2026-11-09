---
symbol: "TMEM202-AS1"
type: "gene"
col: 15344
ensembl_id: "ENSG00000261423"
name: "TMEM202 antisense RNA 1"
location: "15q24.1"
module: 10
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 6
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM202-AS1

*TMEM202 antisense RNA 1* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.32× (z +26.5, q 0e+00, up in 36 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.587× (z -5.0, q 3e-04, down in 13 of 44 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.672× (z -3.5, q 0.044, down in 11 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0739×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Hesperidin (drug)]] 5 µM in 1 line (HEC-1-A 0.0687×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (PANC-1 0.0620×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS6-AS1]] (+0.90, fdr 7e-06), [[PCNX4-DT]] (+0.90, fdr 7e-06), [[OXA1L-DT]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.32×** | +26.5 | 0e+00 | 36/36 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.31×** | +22.3 | 0e+00 | 33/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.56×** | +14.3 | 4e-44 | 32/33 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +12.5 | 2e-33 | 22/31 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +9.2 | 4e-18 | 26/36 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +8.9 | 5e-17 | 4/6 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.6 | 5e-16 | 23/45 (A-172, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.86×** | +8.3 | 6e-15 | 19/45 (A498, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +7.9 | 3e-13 | 2/5 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.22×** | +7.1 | 6e-11 | 22/43 (A-172, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +6.8 | 6e-10 | 8/18 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +6.7 | 1e-09 | 18/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +5.4 | 2e-06 | 4/16 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +5.0 | 2e-05 | 13/40 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.69×** | +4.7 | 9e-05 | 14/45 (LoVo, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.5 | 2e-04 | 7/42 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.39×** | +4.4 | 4e-04 | 8/45 (SW480, LoVo, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.001 | 8/42 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.8 | 0.004 | 13/44 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15344.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 0.0739×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Hesperidin (drug)]] 5 µM in 1 line (HEC-1-A 0.0687×); [[Mozavaptan (drug)]] 0.05 µM in 1 line (PANC-1 0.0620×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.587×** | -5.0 | 3e-04 | 13/44 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.613×** | -4.6 | 0.001 | 14/45 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.612×** | -4.4 | 0.002 | 15/46 (J82, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.640×** | -4.0 | 0.010 | 16/44 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -3.5 | 0.044 | 11/43 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.703×** | -3.3 | 0.088 | 3/42 (HCT15, C32, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.05 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +14.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0739× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 3.66 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.20× (z +9.5) | [[Digitoxin (drug)]] 0.05 µM 0.0719× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 5.80 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +9.5) | [[Hesperidin (drug)]] 5 µM 0.0687× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 4.55 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 2.86 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.29× (z +11.2) | [[Mozavaptan (drug)]] 0.05 µM 0.0620× (z -9.6) |
| [[SW480 (line)]] | alt | 3.42 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +11.1) | — |
| [[A-172 (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +8.9) | — |
| [[A498 (line)]] | wt | 4.25 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 4.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.1× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.76× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 3.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 9.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 3.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 4.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.9) | — |
| [[A-427 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6-AS1]] | +0.90 | +0.91 / +0.73 | both halves | 7e-06 | same gene group |
| [[PCNX4-DT]] | +0.90 | +0.91 / +0.67 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.89 | +0.89 / +0.64 | both halves | 7e-06 |  |
| [[SEPTIN7-DT]] | +0.89 | +0.89 / +0.65 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.88 | +0.88 / +0.58 | both halves | 7e-06 | same gene group |
| [[PPP1R12A-AS2]] | +0.88 | +0.88 / +0.50 | both halves | 1e-05 | same gene group |
| [[ATE1OSP]] | +0.86 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[NEB]] | +0.86 | +0.86 / +0.64 | both halves | 7e-06 |  |
| [[USP38-DT]] | +0.86 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.85 | +0.88 / +0.69 | both halves | 7e-06 |  |
| [[LRRC37A3]] | +0.85 | +0.87 / +0.39 | both halves | 5e-05 |  |
| [[MMADHC-DT]] | +0.85 | +0.85 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM202-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCA10]] | B | ABCA10 activity raises TMEM202-AS1's level | lines that do not express ABCA10 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without ABCA10 | 0.035 | ⚠ within organs, on part of the lines; also absent: ABCA5, S100A6, HLA-H |
| [[SSPN]] | B | SSPN activity raises TMEM202-AS1's level | lines that do not express SSPN (15) vs lines expressing it (35) | 1.24× lower at baseline in the lines without SSPN | 0.045 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[LINC01762]] | B | LINC01762 activity raises TMEM202-AS1's level | lines that do not express LINC01762 (5) vs lines expressing it (45) | 1.49× lower at baseline in the lines without LINC01762 | 0.050 | ⚠ within organs, on part of the lines; also absent: MPP4, LINC01429, DNAH6; maybe low, not absent |
| [[CRPPA]] | B | CRPPA activity lowers TMEM202-AS1's level | lines that do not express CRPPA (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without CRPPA | 0.060 | ⚠ within organs, on part of the lines; also absent: TBL1X, NLGN2; maybe low, not absent; its own permutation p |
| [[KATNAL2]] | B | KATNAL2 activity raises TMEM202-AS1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without KATNAL2 | 0.067 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[ANKRD18B]] | B | ANKRD18B activity raises TMEM202-AS1's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.16× lower at baseline in the lines without ANKRD18B | 0.068 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |
| [[HDAC6]] | B | HDAC6 activity raises TMEM202-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises TMEM202-AS1's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without EFCAB6 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises TMEM202-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without CYP1B1-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TMEM202-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[LRRIQ3]] | C | LRRIQ3 activity raises TMEM202-AS1's level | lines that do not express LRRIQ3 (4) vs lines expressing it (46) | 1.28× lower at baseline in the lines without LRRIQ3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENTPD1-AS1, CEP41, C1orf216; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.885). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.8, 15.6); signed map (26.9, -9.0). **Vector** length 84.5, 15.9% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +26.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +22.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -6.0 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.1 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -4.4 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | TMEM202 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q24.1 — chr15:72,407,778-72,475,168 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53265) · Entrez [105370888](https://www.ncbi.nlm.nih.gov/gene/105370888) · Ensembl [ENSG00000261423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261423)

## Data

Gene col 15344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15344); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15344]; `tensor/DDL_lfc|DDL_z.npy` [15344]; `embed/gene_vectors.npy` [15344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15344 or target_col == 15344). Every well: [[TMEM202-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM202-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "UBAP1L"
type: "gene"
col: 14475
ensembl_id: "ENSG00000246922"
name: "ubiquitin associated protein 1 like"
location: "15q22.31"
module: 37
arm: "+"
pooled_cpm: 7.6
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# UBAP1L

*ubiquitin associated protein 1 like* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.78× (z +18.0, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.645× (z -4.2, q 0.011, down in 20 of 47 measured lines) ⚠ cell-cycle shift, explains ~60% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.660× (z -4.0, q 0.011, down in 19 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.0871×, HEC-1-A 0.105×, CFPAC-1 0.0874×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.134×, NCI-H1573 0.0662×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0792×); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0625×); [[Sunitinib (drug)]] 0.5 µM in 1 line (A-172 0.0725×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM269]] (+0.71, fdr 7e-06), [[SMIM15-AS1]] (+0.69, fdr 7e-06), [[MIRLET7IHG]] (+0.69, fdr 1e-05); moves opposite to [[NAA40]] (-0.59, fdr 2e-05), [[PAFAH1B3]] (-0.59, fdr 3e-05), [[HPF1]] (-0.59, fdr 4e-04).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.78×** | +18.0 | 0e+00 | 43/44 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +9.3 | 5e-18 | 29/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +9.2 | 1e-17 | 35/42 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +8.5 | 3e-15 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +7.0 | 3e-10 | 28/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +6.1 | 1e-07 | 28/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +6.0 | 2e-07 | 16/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +5.5 | 2e-06 | 25/47 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.1 | 2e-05 | 18/47 (HOP62, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.35×** | +4.0 | 0.003 | 13/48 (Panc 03.27, HT-29, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.0 | 0.004 | 18/42 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.009 | 10/48 (RKO, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.009 | 14/45 (LoVo, HOP62, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.009 | 13/47 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.010 | 12/46 (A549, NCI-H1573, …) | two highest doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.053 | 6/47 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.058 | 11/47 (SNU-423, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LoVo 0.0871×, HEC-1-A 0.105×, CFPAC-1 0.0874×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.134×, NCI-H1573 0.0662×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.0792×); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (Panc 03.27 0.0625×); [[Sunitinib (drug)]] 0.5 µM in 1 line (A-172 0.0725×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.645×** | -4.2 | 0.011 | 20/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.647×** | -4.0 | 0.011 | 18/46 (NCI-H2030, SNU-423, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.011 | 19/47 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.660×** | -3.9 | 0.015 | 14/47 (SW 1271, NCI-H1792, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.673×** | -3.8 | 0.015 | 16/43 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | 0.714× | -3.3 | 0.11 | 20/32 (LoVo, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.724× | -3.1 | 0.14 | 18/46 (HS-578T, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.53 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.70× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0989× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[LoVo (line)]] | wt | 22.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 7.90 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 7.35 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0874× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[NCI-H23 (line)]] | alt | 11.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.3) | [[Auranofin (drug)]] 5 µM 0.0792× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 6.18 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +9.3) | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0625× (z -9.3) |
| [[A-172 (line)]] | wt | 4.94 | 0 | 1 | — | [[Sunitinib (drug)]] 0.5 µM 0.0725× (z -8.8) |
| [[A549 (line)]] | wt | 5.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.42× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 6.13 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0886× (z -8.6) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 8.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 8.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 5.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 7.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H1792 (line)]] | alt | 9.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.00× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0942× (z -8.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM269]] | +0.71 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[MIRLET7IHG]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[TMED6]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.68 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[DNHD1]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[RRH]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TRPV1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[QRICH2]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SLC23A3]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MYH3]] | +0.66 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[ZNF213-AS1]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA40]] | -0.59 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PAFAH1B3]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[HPF1]] | -0.59 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[ARRB2]] | -0.59 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[COMMD8]] | -0.58 | -0.18 / -0.66 | ⚠ one half (not replicated) | 9e-04 |  |
| [[SMARCD3]] | -0.57 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[PHF6]] | -0.56 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[KCTD17]] | -0.56 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBAP1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.9, -15.6); signed map (14.4, 2.9). **Vector** length 70.7, 12.2% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin associated protein 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:65,092,760-65,115,200 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [F5GYI3](https://www.uniprot.org/uniprotkb/F5GYI3) carries no function annotation.

**Summary**, from NCBI Gene [390595](https://www.ncbi.nlm.nih.gov/gene/390595):

> Predicted to enable ubiquitin binding activity. Predicted to be involved in ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway. Predicted to be part of ESCRT I complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:40028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40028) · Entrez [390595](https://www.ncbi.nlm.nih.gov/gene/390595) · UniProt [F5GYI3](https://www.uniprot.org/uniprotkb/F5GYI3) · Ensembl [ENSG00000246922](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246922)

## Data

Gene col 14475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14475); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14475]; `tensor/DDL_lfc|DDL_z.npy` [14475]; `embed/gene_vectors.npy` [14475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14475 or target_col == 14475). Every well: [[UBAP1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAP1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

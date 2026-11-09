---
symbol: "PPP1R12A-AS2"
type: "gene"
col: 15080
ensembl_id: "ENSG00000258048"
name: "PPP1R12A antisense RNA 2"
location: "12q21.2"
module: 23
arm: "+"
pooled_cpm: 8.19
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# PPP1R12A-AS2

*PPP1R12A antisense RNA 2* — 12q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.3× (z +36.8, q 0e+00, up in 41 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0635×); [[Nafamostat (mesylate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0709×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATE1OSP]] (+0.89, fdr 7e-06), [[TMEM202-AS1]] (+0.88, fdr 1e-05), [[INTS6-AS1]] (+0.87, fdr 7e-06); moves opposite to [[MAST3]] (-0.74, fdr 7e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[OTS514 (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.3×** | +36.8 | 0e+00 | 41/42 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **7.30×** | +31.3 | 0e+00 | 42/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.53×** | +16.2 | 0e+00 | 38/40 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.50×** | +14.0 | 3e-42 | 40/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.66×** | +13.9 | 7e-42 | 38/42 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.03×** | +11.2 | 6e-27 | 33/48 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.83×** | +11.1 | 6e-27 | 34/45 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.29×** | +9.3 | 2e-18 | 30/45 (HT-29, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.8 | 1e-16 | 7/16 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +7.9 | 1e-13 | 12/25 (LoVo, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.8 | 5e-10 | 13/31 (Hs 766T, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +6.1 | 4e-08 | 26/46 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.6 | 2e-04 | 18/37 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.28×** | +3.9 | 0.003 | 13/46 (BT-474, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 10/47 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.009 | 14/46 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.011 | 10/47 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.011 | 12/47 (A-172, HOP62, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.013 | 12/46 (SNU-423, A-172, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.053 | 12/46 (BT-474, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15080.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ponatinib (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0635×); [[Nafamostat (mesylate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0709×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.823× | -3.0 | 0.71 | 7/47 (CHP-212, PANC-1, …) | all doses, flat | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 0.761× | -3.0 | 0.71 | 16/43 (A-427, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.92 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +16.2) | — |
| [[LoVo (line)]] | wt | 8.08 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 6.08 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +20.0) | — |
| [[SW480 (line)]] | alt | 6.24 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +16.1) | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.6) | [[Ponatinib (drug)]] 0.5 µM 0.0635× (z -11.2) |
| [[HOP62 (line)]] | alt | 5.18 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +16.4) | — |
| [[HS-578T (line)]] | alt | 5.53 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 5.99 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.1× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 9.46 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.18× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 12.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 8.76 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +14.1) | — |
| [[A498 (line)]] | wt | 8.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +16.5) | — |
| [[BT-474 (line)]] | alt | 14.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.5) | — |
| [[C32 (line)]] | wt | 4.35 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 5.22 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 7.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.4× (z +12.8) | — |
| [[H4 (line)]] | wt | 8.23 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +11.1) | — |
| [[HCT15 (line)]] | alt | 8.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 4.26 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.8× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 9.41 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +15.1) | — |
| [[J82 (line)]] | alt | 6.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.98× (z +13.4) | — |
| [[KATO III (line)]] | alt | 8.67 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.60× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 5.96 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 4.55 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.94 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 14.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +18.5) | — |
| [[SK-MEL-2 (line)]] | alt | 4.38 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 17.8× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 6.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +12.0) | — |
| [[SW48 (line)]] | wt | 6.53 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +11.6) | — |
| [[A549 (line)]] | wt | 7.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +13.8) | — |
| [[AsPC-1 (line)]] | alt | 3.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.7× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 8.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.46× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.81× (z +13.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 6.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +16.0) | — |
| [[RKO (line)]] | wt | 5.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 5.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 5.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +13.8) | — |
| [[A-427 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | +0.89 | +0.87 / +0.62 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.88 | +0.88 / +0.50 | both halves | 1e-05 | same gene group |
| [[INTS6-AS1]] | +0.87 | +0.87 / +0.64 | both halves | 7e-06 | same gene group |
| [[PKN2-AS1]] | +0.86 | +0.87 / +0.45 | both halves | 3e-05 | same gene group |
| [[MMADHC-DT]] | +0.85 | +0.86 / +0.40 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | +0.85 | +0.83 / +0.52 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.84 | +0.85 / +0.55 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.84 | +0.84 / +0.47 | both halves | 2e-05 |  |
| [[NEB]] | +0.84 | +0.86 / +0.56 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.83 | +0.83 / +0.45 | both halves | 3e-05 |  |
| [[PBLD]] | +0.83 | +0.83 / +0.24 | both halves | 5e-04 |  |
| [[MAILR]] | +0.83 | +0.85 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.74 | -0.67 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPP1R12A-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00944]] | B | LINC00944 activity lowers PPP1R12A-AS2's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.39× higher at baseline in the lines without LINC00944 | 0.052 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[AGA-DT]] | B | AGA-DT activity raises PPP1R12A-AS2's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without AGA-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[RNF217-AS1]] | B | RNF217-AS1 activity lowers PPP1R12A-AS2's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 1.24× higher at baseline in the lines without RNF217-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[OTS514 (drug)]] 0.05 µM | C | PPP1R12A-AS2's natural level lowers the cells' numbers under OTS514 0.05 µM (makes them more sensitive) | PPP1R12A-AS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.081 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.891). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (7.6, 13.5); signed map (24.4, -7.0). **Vector** length 92.8, 20.0% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +36.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.2 | +31.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +14.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +16.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R12A antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q21.2 — chr12:79,690,144-79,778,451 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55456) · Entrez [105369864](https://www.ncbi.nlm.nih.gov/gene/105369864) · Ensembl [ENSG00000258048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258048)

## Data

Gene col 15080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15080); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15080]; `tensor/DDL_lfc|DDL_z.npy` [15080]; `embed/gene_vectors.npy` [15080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15080 or target_col == 15080). Every well: [[PPP1R12A-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R12A-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

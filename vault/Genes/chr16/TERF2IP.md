---
symbol: "TERF2IP"
type: "gene"
col: 9371
ensembl_id: "ENSG00000166848"
name: "TERF2 interacting protein"
location: "16q23.1"
module: 20
arm: "-"
pooled_cpm: 86.19
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# TERF2IP

*TERF2 interacting protein* — 16q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +12.2, q 2e-31, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +10.2, q 5e-22, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.649× (z -4.9, q 7e-04, down in 44 of 48 measured lines) ⚠ unreliable plate only.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM5]] (+0.85, fdr 7e-06), [[NDUFC1]] (+0.76, fdr 7e-06), [[CIR1]] (+0.75, fdr 7e-06); moves opposite to [[PRKDC]] (-0.79, fdr 7e-06), [[MTHFD1]] (-0.73, fdr 7e-06), [[EFTUD2]] (-0.72, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GPRC5C]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CS]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9371.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.15×** | +12.2 | 2e-31 | 46/48 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +10.2 | 5e-22 | 49/49 (BT-474, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.8 | 2e-16 | 46/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +8.1 | 1e-13 | 47/48 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.00×** | +7.8 | 6e-13 | 44/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.92×** | +7.1 | 1e-10 | 43/48 (HOP62, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +6.2 | 4e-08 | 42/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.62×** | +5.4 | 4e-06 | 41/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.013 | 27/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +3.6 | 0.017 | 30/48 (SW480, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.074 | 25/48 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9371.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -4.9 | 7e-04 | 44/48 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.819× | -3.2 | 0.40 | 27/48 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.826× | -3.0 | 0.40 | 19/48 (LOX-IMVI, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9371. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 120 | 6 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.96× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.84× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 82.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.15× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 67.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +12.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.98× (z +11.1) | — |
| [[PANC-1 (line)]] | alt | 43.6 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.0) | — |
| [[A-172 (line)]] | wt | 104 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 65.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 76.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 87.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.1) | — |
| [[LoVo (line)]] | wt | 43.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 96.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 56.2 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.87× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.46× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 90.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.0) | — |
| [[A-427 (line)]] | wt | 52.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.94× (z +10.2) | — |
| [[A549 (line)]] | wt | 66.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +11.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.4) | — |
| [[C32 (line)]] | wt | 101 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 81.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.66× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 96.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 74.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 93.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.0) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 81.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 75.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +9.2) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 98.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +10.9) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 67.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.1) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 96.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 90.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.7) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1792 (line)]] | alt | 92.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 70.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 50.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 92.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.2) | — |
| [[SNU-423 (line)]] | alt | 79.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.5) | — |
| [[SW48 (line)]] | wt | 74.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9371), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | +0.85 | +0.83 / +0.83 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.76 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[CIR1]] | +0.75 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[EAPP]] | +0.75 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[TMEM258]] | +0.75 | +0.62 / +0.81 | both halves | 7e-06 |  |
| [[NKAP]] | +0.74 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[CDC37L1]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[NR1H3]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[SYF2]] | +0.73 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[RSF1]] | +0.73 | +0.80 / +0.60 | both halves | 7e-06 | pathway: Chromosome Maintenance |
| [[POLR1H]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.72 | +0.60 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.79 | -0.73 / -0.75 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.73 | -0.68 / -0.72 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.72 | -0.67 / -0.74 | both halves | 7e-06 |  |
| [[ICMT]] | -0.72 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.72 | -0.70 / -0.68 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[PRPS1]] | -0.71 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[CCT5]] | -0.71 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.69 | -0.64 / -0.69 | both halves | 7e-06 |  |
| [[YWHAQ]] | -0.69 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[RPE]] | -0.68 | -0.61 / -0.73 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.68 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[IPO5]] | -0.68 | -0.62 / -0.73 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5C]] | B | GPRC5C activity lowers TERF2IP's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.17× higher at baseline in the lines without GPRC5C | 0.088 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CS]] | C | TERF2IP's natural level weakens CS's drug response | TERF2IP's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.03; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.3, -31.4); signed map (-6.8, 4.9). **Vector** length 114, 40.8% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +5.5 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +8.1 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +3.0 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.0 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.5 | +1.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.5 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TERF2 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.1 — chr16:75,647,773-75,761,872 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAP1 |
| Gene groups (HGNC) | Shelterin complex |
| Reactome | 28 pathways, smallest: Telomere C-strand synthesis initiation; Removal of the Flap Intermediate from the C-strand; Packaging Of Telomere Ends |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYB0](https://www.uniprot.org/uniprotkb/Q9NYB0) (Telomeric repeat-binding factor 2-interacting protein 1):

> Acts both as a regulator of telomere function and as a transcription regulator. Involved in the regulation of telomere length and protection as a component of the shelterin complex (telosome). In contrast to other components of the shelterin complex, it is dispensible for telomere capping and does not participate in the protection of telomeres against non-homologous end-joining (NHEJ)-mediated repair. Instead, it is required to negatively regulate telomere recombination and is essential for …

**Summary**, from NCBI Gene [54386](https://www.ncbi.nlm.nih.gov/gene/54386):

> Enables G-rich strand telomeric DNA binding activity and phosphatase binding activity. Involved in several processes, including negative regulation of telomere maintenance; protection from non-homologous end joining at telomere; and protein localization to chromosome, telomeric region. Located in chromosome, telomeric region; cytoplasm; and nucleus. Part of shelterin complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19246) · Entrez [54386](https://www.ncbi.nlm.nih.gov/gene/54386) · UniProt [Q9NYB0](https://www.uniprot.org/uniprotkb/Q9NYB0) · Ensembl [ENSG00000166848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166848)

## Data

Gene col 9371: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9371); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9371, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9371]; `tensor/DDL_lfc|DDL_z.npy` [9371]; `embed/gene_vectors.npy` [9371]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9371 or target_col == 9371). Every well: [[TERF2IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TERF2IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

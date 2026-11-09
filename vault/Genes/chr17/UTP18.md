---
symbol: "UTP18"
type: "gene"
col: 231
ensembl_id: "ENSG00000011260"
name: "UTP18 small subunit processome component"
location: "17q21.33"
module: 33
arm: "+"
pooled_cpm: 51.09
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# UTP18

*UTP18 small subunit processome component* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.72× (z +11.5, q 1e-27, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.717× (z -7.9, q 1e-12, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR3]] (+0.75, fdr 7e-06), [[WDR36]] (+0.75, fdr 7e-06), [[URI1]] (+0.72, fdr 7e-06); moves opposite to [[DYNLL1]] (-0.59, fdr 1e-05), [[OFD1]] (-0.58, fdr 1e-05), [[HMGCL]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +11.5 | 1e-27 | 45/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +11.3 | 3e-27 | 42/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.64×** | +11.3 | 3e-27 | 42/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +8.1 | 7e-14 | 34/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +7.6 | 4e-12 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.3 | 3e-11 | 35/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +6.4 | 1e-08 | 32/48 (NCI-H460, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +6.2 | 4e-08 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 4e-05 | 27/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.4 | 5e-04 | 25/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.007 | 20/48 (A549, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.013 | 15/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.029 | 16/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.038 | 20/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.1 | 0.062 | 16/44 (NCI-H460, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.093 | 11/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -7.9 | 1e-12 | 31/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -4.7 | 5e-04 | 29/47 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.821×** | -4.7 | 5e-04 | 21/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -4.3 | 0.002 | 22/44 (A549, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -4.2 | 0.002 | 24/48 (RKO, SNU-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.9 | 0.007 | 20/48 (A498, A-427, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.799×** | -3.8 | 0.012 | 20/47 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.043 | 20/47 (NCI-H23, A-427, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.046 | 20/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.820×** | -3.4 | 0.046 | 20/48 (MIA PaCa-2, LS 180, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.862× | -3.3 | 0.048 | 9/48 (SW480, hTERT-HPNE, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.824×** | -3.3 | 0.052 | 15/48 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.057 | 14/48 (A498, RPMI-7951, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.829×** | -3.2 | 0.060 | 12/47 (A-427, NCI-H1573, …) | two highest doses | low cells (technical?) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.829×** | -3.1 | 0.085 | 13/49 (SW 1271, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.0 | 0.085 | 19/48 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 75.0 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 41.2 | 6 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.28× (z +11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.22× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 34.9 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.83× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 61.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.25× (z +10.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.60× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 83.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 57.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 37.3 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.58× (z +8.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 5.66× (z +8.7) | — |
| [[RKO (line)]] | wt | 62.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -15.1) |
| [[A-427 (line)]] | wt | 68.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 69.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -15.6) |
| [[A549 (line)]] | wt | 60.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.8) |
| [[COLO 205 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.31× (z +10.1) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 52.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.5) |
| [[J82 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.44× (z +8.7) ⚠ toxic | — |
| [[KATO III (line)]] | alt | 61.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.89× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 68.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -9.1) |
| [[SNU-1 (line)]] | wt | 74.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.7) |
| [[SW480 (line)]] | alt | 51.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -8.8) |
| [[A-172 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR3]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[WDR36]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[URI1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[DFFB]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DKC1]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 521 |
| [[POLR1B]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 | STRING 761 |
| [[DDX54]] | +0.70 | +0.69 / +0.67 | both halves | 7e-06 | STRING 511 |
| [[NSUN2]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 | STRING 540 |
| [[IPO11]] | +0.69 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[MDN1]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[AHCTF1]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[GTPBP3]] | +0.69 | +0.72 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNLL1]] | -0.59 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[OFD1]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.57 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[WBP4]] | -0.57 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[LRCH3]] | -0.57 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UTP18's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.9, -38.9); signed map (-6.6, -51.6). **Vector** length 94.0, 25.9% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.0 | +11.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.6 | +0.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | -3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +11.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | -4.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.2 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.1 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | +0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | UTP18 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:51,260,546-51,297,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-48; previously WDR50 |
| Gene groups (HGNC) | WD repeat domain containing; UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5J1](https://www.uniprot.org/uniprotkb/Q9Y5J1) (U3 small nucleolar RNA-associated protein 18 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in nucleolar processing of pre-18S ribosomal RNA.

**Summary**, from NCBI Gene [51096](https://www.ncbi.nlm.nih.gov/gene/51096):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24274) · Entrez [51096](https://www.ncbi.nlm.nih.gov/gene/51096) · UniProt [Q9Y5J1](https://www.uniprot.org/uniprotkb/Q9Y5J1) · Ensembl [ENSG00000011260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011260)

## Data

Gene col 231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 231); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 231]; `tensor/DDL_lfc|DDL_z.npy` [231]; `embed/gene_vectors.npy` [231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 231 or target_col == 231). Every well: [[UTP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

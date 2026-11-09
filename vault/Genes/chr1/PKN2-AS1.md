---
symbol: "PKN2-AS1"
type: "gene"
col: 14138
ensembl_id: "ENSG00000237505"
name: "PKN2 antisense RNA 1"
location: "1p22.2"
module: 26
arm: "+"
pooled_cpm: 9.84
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PKN2-AS1

*PKN2 antisense RNA 1* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.1× (z +35.5, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.524× (z -7.0, q 1e-09, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.635× (z -4.9, q 1e-04, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAD2L1-DT]] (+0.89, fdr 7e-06), [[TMEM202-AS1]] (+0.88, fdr 7e-06), [[PCNX4-DT]] (+0.88, fdr 8e-06); moves opposite to [[MAST3]] (-0.76, fdr 4e-05), [[FAM118A]] (-0.75, fdr 2e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC00276]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14138.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.1×** | +35.5 | 0e+00 | 44/45 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +20.3 | 0e+00 | 40/44 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.84×** | +16.5 | 0e+00 | 41/42 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.79×** | +15.8 | 0e+00 | 41/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.24×** | +15.1 | 0e+00 | 41/43 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.84×** | +11.3 | 7e-28 | 41/47 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.76×** | +11.1 | 1e-26 | 32/43 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +9.2 | 3e-18 | 28/47 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.9 | 2e-07 | 8/19 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +5.8 | 4e-07 | 11/25 (SW 900, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +5.5 | 2e-06 | 25/46 (HT-29, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 20/46 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +5.0 | 2e-05 | 20/46 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +4.9 | 4e-05 | 17/35 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **1.34×** | +4.5 | 2e-04 | 14/47 (HS-578T, A-172, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.007 | 11/46 (A498, hTERT-HPNE, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.009 | 9/45 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.009 | 9/48 (SW 900, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14138.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.524×** | -7.0 | 1e-09 | 31/47 (COLO 205, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.611×** | -5.3 | 2e-05 | 24/47 (J82, A549, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.612×** | -5.3 | 2e-05 | 20/47 (SK-MEL-2, SW 1271, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -5.2 | 3e-05 | 21/47 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.635×** | -4.9 | 1e-04 | 20/47 (NCI-H23, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.655×** | -4.6 | 4e-04 | 20/47 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.663×** | -4.4 | 7e-04 | 21/44 (HEC-1-A, Hs 766T, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -4.3 | 0.001 | 18/42 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.680×** | -3.9 | 0.005 | 15/43 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.698×** | -3.9 | 0.006 | 17/47 (J82, HT-29, …) | rises with dose | composition shift |
| [[Sunitinib (drug)]] 0.05 µM |  | **0.738×** | -3.3 | 0.059 | 7/47 (C32, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14138. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 7.34 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +16.9) | — |
| [[SHP-77 (line)]] | alt | 16.7 | 5 (1 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 5.84× (z +10.4) | — |
| [[A-172 (line)]] | wt | 6.65 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +13.9) | — |
| [[C32 (line)]] | wt | 10.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +15.3) | [[Bendamustine (drug)]] 5 µM 0.0719× (z -10.3) |
| [[HOP62 (line)]] | alt | 8.00 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 9.26 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +16.7) | — |
| [[LoVo (line)]] | wt | 6.42 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +18.6) | — |
| [[NCI-H460 (line)]] | wt | 4.47 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +16.2) | — |
| [[PANC-1 (line)]] | alt | 8.69 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +20.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.72 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.237× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 17.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 8.28 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.16× (z +16.3) | — |
| [[A549 (line)]] | wt | 6.98 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +11.7) | — |
| [[C-33 A (line)]] | alt | 11.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 9.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 4.65 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +14.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.09 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +13.0) | [[Tadalafil (drug)]] 5 µM 0.0709× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 8.56 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 5.31 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +14.8) | — |
| [[A498 (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 7.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.4× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 7.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.6× (z +15.3) | — |
| [[BT-474 (line)]] | alt | 5.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 8.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 5.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.2× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +11.7) | — |
| [[J82 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.17× (z +13.0) | — |
| [[KATO III (line)]] | alt | 8.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 6.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.3× (z +16.3) | — |
| [[NCI-H1573 (line)]] | alt | 17.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 4.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.71× (z +10.7) | — |
| [[RKO (line)]] | wt | 4.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.8× (z +13.2) | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 13.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.43× (z +12.0) | — |
| [[A-427 (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14138), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD2L1-DT]] | +0.89 | +0.88 / +0.61 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.88 | +0.88 / +0.58 | both halves | 7e-06 | same gene group |
| [[PCNX4-DT]] | +0.88 | +0.89 / +0.58 | both halves | 8e-06 |  |
| [[CFAP418-AS1]] | +0.86 | +0.83 / +0.71 | both halves | 7e-06 | same gene group |
| [[MMADHC-DT]] | +0.86 | +0.84 / +0.57 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.86 | +0.87 / +0.45 | both halves | 3e-05 | same gene group |
| [[CCDC90B-AS1]] | +0.85 | +0.80 / +0.55 | both halves | 1e-05 | same gene group |
| [[CHD1-DT]] | +0.84 | +0.83 / +0.58 | both halves | 7e-06 |  |
| [[MAILR]] | +0.83 | +0.86 / +0.39 | both halves | 6e-05 |  |
| [[INTS6-AS1]] | +0.82 | +0.84 / +0.55 | both halves | 1e-05 | same gene group |
| [[NEB]] | +0.81 | +0.83 / +0.50 | both halves | 1e-05 |  |
| [[OXA1L-DT]] | +0.80 | +0.81 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.76 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[FAM118A]] | -0.75 | -0.66 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00276]] | B | LINC00276 activity raises PKN2-AS1's level | lines that do not express LINC00276 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without LINC00276 | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC02932, MGC4859, RBFOX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PKN2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[COP1-DT]] | B | COP1-DT activity raises PKN2-AS1's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without COP1-DT | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.878). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (7.8, 14.5); signed map (27.1, -9.0). **Vector** length 107, 25.8% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +35.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +11.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +20.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.5 | +15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +5.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +5.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -8.0 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -7.5 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -6.8 | -5.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.9 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | PKN2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p22.2 — chr1:87,620,803-88,685,204 (-) |
| Ensembl biotype | lncRNA |
| Also known as | uc.31 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50597) · Entrez [101927891](https://www.ncbi.nlm.nih.gov/gene/101927891) · Ensembl [ENSG00000237505](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237505)

## Data

Gene col 14138: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14138); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14138, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14138]; `tensor/DDL_lfc|DDL_z.npy` [14138]; `embed/gene_vectors.npy` [14138]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14138 or target_col == 14138). Every well: [[PKN2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKN2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

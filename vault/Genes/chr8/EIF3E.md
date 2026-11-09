---
symbol: "EIF3E"
type: "gene"
col: 2455
ensembl_id: "ENSG00000104408"
name: "eukaryotic translation initiation factor 3 subunit E"
location: "8q23.1"
module: 43
arm: "+"
pooled_cpm: 218.73
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# EIF3E

*eukaryotic translation initiation factor 3 subunit E* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.98× (z +12.0, q 3e-30, up in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.81× (z +10.8, q 9e-25, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.930× (z -4.3, q 0.009, down in 0 of 50 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.417×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.512×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.689×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NACA]] (+0.68, fdr 7e-06, ⚠ NACA in the vector space only through flagged drug-doses), [[MRPS30]] (+0.66, fdr 7e-06), [[TAF1D]] (+0.63, fdr 1e-05), [[BTF3]] (+0.62, fdr 7e-06); moves opposite to [[RB1]] (-0.57, fdr 1e-05), [[AP1B1]] (-0.52, fdr 5e-05), [[IER2]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2455.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +12.0 | 3e-30 | 44/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.81×** | +10.8 | 9e-25 | 48/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +9.8 | 1e-20 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.53×** | +8.9 | 1e-16 | 42/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +8.5 | 1e-15 | 45/48 (PANC-1, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +8.2 | 2e-14 | 45/49 (RKO, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +7.5 | 6e-12 | 44/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +7.5 | 6e-12 | 43/48 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.4 | 8e-09 | 44/45 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 2e-06 | 32/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 3e-06 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.34×** | +5.4 | 4e-06 | 36/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.1 | 2e-05 | 30/38 (NCI-H1573, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +4.7 | 1e-04 | 27/48 (NCI-H1792, NCI-H1573, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.61×** | +4.5 | 2e-04 | 38/47 (C32, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +4.5 | 2e-04 | 36/48 (A498, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 18/49 (SNU-1, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 3e-04 | 39/49 (PANC-1, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.002 | 32/48 (A498, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.013 | 32/48 (A498, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.018 | 22/48 (PANC-1, A498, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.028 | 20/48 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2455.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (BT-474 0.417×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.512×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.689×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.3 | 0.009 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.799×** | -4.1 | 0.011 | 29/48 (PANC-1, A498, …) | all doses, flat |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.5 | 0.10 | 21/48 (Panc 03.27, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.841× | -3.2 | 0.22 | 21/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 226 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +14.0) | — |
| [[NCI-H460 (line)]] | wt | 191 | 6 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.98× (z +13.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 159 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +18.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +9.2) | — |
| [[RKO (line)]] | wt | 517 | 4 (1 ⚠) | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.16× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 169 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 151 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.10× (z +13.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +12.0) | — |
| [[J82 (line)]] | alt | 189 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.60× (z +11.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +9.5) | — |
| [[A498 (line)]] | wt | 305 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.11× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 229 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.51× (z +9.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.69× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 142 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.64× (z +20.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +11.1) | — |
| [[Hs 766T (line)]] | wt | 189 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.73× (z +11.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[KATO III (line)]] | alt | 170 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +13.8) | — |
| [[LoVo (line)]] | wt | 231 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.23× (z +14.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 234 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +10.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 3.38× (z +9.4) | — |
| [[SW480 (line)]] | alt | 206 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.3) | — |
| [[A-172 (line)]] | wt | 100 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[C32 (line)]] | wt | 221 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 191 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 173 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.34× (z +8.5) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 247 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 230 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 322 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 178 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.23× (z +10.2) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 319 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 178 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 252 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.08× (z +9.3) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.47× (z +10.4) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 209 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.1) | — |
| [[A-427 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 225 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 234 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 278 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 251 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 156 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 427 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 244 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 272 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACA]] ⚠ | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS30]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[TAF1D]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[BTF3]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | STRING 466 |
| [[MRPS35]] | +0.60 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SUPV3L1]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[RPL5]] | +0.60 | +0.60 / +0.66 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 717 |
| [[DDX54]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[RPL22]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 557 |
| [[RPL7]] | +0.57 | +0.62 / +0.59 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 704 |
| [[NPM1]] | +0.57 | +0.56 / +0.57 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 702 |
| [[EEF1B2]] | +0.56 | +0.66 / +0.45 | both halves | 3e-05 | STRING 777 |
| [[TMCC1-DT]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RB1]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[AP1B1]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[IER2]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TMEM107]] | -0.49 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[AKIRIN1]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SCYL2]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PRKACA]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PDLIM7]] | -0.47 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-43.4, -30.8); signed map (-32.9, -20.9). **Vector** length 103, 38.6% of its response variance represented; |z| ≥ 3 in 1,211 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.4 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.5 | +7.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.3 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.2 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | +5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | +9.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.6 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -0.6 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.7 | -1.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 3 subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:108,162,787-108,443,496 (-) |
| Ensembl biotype | protein_coding |
| Also known as | eIF3-p48; previously INT6, EIF3S6 |
| Gene groups (HGNC) | Eukaryotic translation initiation factor 3 complex subunits |
| Reactome | 14 pathways, smallest: Formation of the ternary complex, and subsequently, the 43S complex; Ribosomal scanning and start codon recognition; Translation initiation complex formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P60228](https://www.uniprot.org/uniprotkb/P60228) (Eukaryotic translation initiation factor 3 subunit E):

> Component of the eukaryotic translation initiation factor 3 (eIF-3) complex, which is required for several steps in the initiation of protein synthesis. The eIF-3 complex associates with the 40S ribosome and facilitates the recruitment of eIF-1, eIF-1A, eIF-2:GTP:methionyl-tRNAi and eIF-5 to form the 43S pre-initiation complex (43S PIC). The eIF-3 complex stimulates mRNA recruitment to the 43S PIC and scanning of the mRNA for AUG recognition. The eIF-3 complex is also required for disassembly …

**Summary**, from NCBI Gene [3646](https://www.ncbi.nlm.nih.gov/gene/3646):

> Enables RNA binding activity and cadherin binding activity. Contributes to translation initiation factor activity. Involved in nuclear-transcribed mRNA catabolic process, nonsense-mediated decay; positive regulation of translation; and translational initiation. Located in PML body and cytosol. Part of eukaryotic translation initiation factor 3 complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3277) · Entrez [3646](https://www.ncbi.nlm.nih.gov/gene/3646) · UniProt [P60228](https://www.uniprot.org/uniprotkb/P60228) · Ensembl [ENSG00000104408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104408)

## Data

Gene col 2455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2455); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2455]; `tensor/DDL_lfc|DDL_z.npy` [2455]; `embed/gene_vectors.npy` [2455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2455 or target_col == 2455). Every well: [[EIF3E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF3E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

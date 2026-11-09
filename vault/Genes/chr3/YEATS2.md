---
symbol: "YEATS2"
type: "gene"
col: 8797
ensembl_id: "ENSG00000163872"
name: "YEATS domain containing 2"
location: "3q27.1"
module: 164
arm: "+"
pooled_cpm: 275.32
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# YEATS2

*YEATS domain containing 2* — 3q27.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.256× (z -31.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR45B]] (+0.75, fdr 7e-06), [[PDK3]] (+0.75, fdr 7e-06), [[INSIG2]] (+0.75, fdr 7e-06); moves opposite to [[PPP3CB-AS1]] (-0.55, fdr 8e-05), [[AVEN]] (-0.53, fdr 1e-04), [[ARHGAP42]] (-0.53, fdr 3e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[NCKIPSD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PF-06260933 (drug)]] 5 µM |  | 1.47× | +3.3 | 0.58 | 28/48 (BT-474, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.256×** | -31.0 | 0e+00 | 48/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.333×** | -17.7 | 0e+00 | 47/49 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.326×** | -17.3 | 0e+00 | 43/44 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.362×** | -15.7 | 0e+00 | 47/47 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -15.5 | 0e+00 | 44/49 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.391×** | -14.5 | 1e-45 | 47/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.421×** | -13.9 | 4e-42 | 47/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.440×** | -12.2 | 2e-32 | 44/45 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.549×** | -9.3 | 1e-18 | 45/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.586×** | -8.6 | 5e-16 | 45/48 (NCI-H1792, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.586×** | -8.6 | 5e-16 | 43/48 (CFPAC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.598×** | -8.2 | 8e-15 | 43/48 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.605×** | -8.1 | 3e-14 | 42/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.702×** | -8.0 | 4e-14 | 39/48 (HOP62, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.624×** | -7.3 | 1e-11 | 41/48 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -5.8 | 2e-07 | 30/48 (RKO, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -3.7 | 0.006 | 30/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.799×** | -3.6 | 0.009 | 27/48 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.808×** | -3.4 | 0.014 | 28/48 (A549, HOP62, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.039 | 26/49 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.833×** | -2.9 | 0.068 | 24/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.834× | -2.9 | 0.072 | 21/48 (NCI-H1573, HepG2/C3A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.831×** | -2.8 | 0.084 | 23/48 (NCI-H1573, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 354 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -38.4) |
| [[LOX-IMVI (line)]] | wt | 357 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -31.8) |
| [[A-172 (line)]] | wt | 336 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -30.1) |
| [[HOP62 (line)]] | alt | 382 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -26.8) |
| [[MIA PaCa-2 (line)]] | alt | 570 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -30.8) |
| [[SNU-423 (line)]] | alt | 343 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -26.6) |
| [[HS-578T (line)]] | alt | 361 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -33.3) |
| [[hTERT-HPNE (line)]] | wt | 259 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -32.3) |
| [[NCI-H460 (line)]] | wt | 206 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -30.4) |
| [[RPMI-7951 (line)]] | alt | 428 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -28.8) |
| [[CFPAC-1 (line)]] | alt | 340 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -26.3) |
| [[HEC-1-A (line)]] | alt | 383 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -23.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.383× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 357 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -33.5) |
| [[SK-MEL-2 (line)]] | alt | 396 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -27.5) |
| [[A549 (line)]] | wt | 208 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -20.7) |
| [[BT-474 (line)]] | alt | 233 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -22.2) |
| [[Hs 766T (line)]] | wt | 225 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.9) |
| [[H4 (line)]] | wt | 394 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -24.9) |
| [[PANC-1 (line)]] | alt | 288 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -22.2) |
| [[SW480 (line)]] | alt | 253 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -16.3) |
| [[AN3 CA (line)]] | alt | 301 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -18.3) |
| [[HCT15 (line)]] | alt | 431 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.8) |
| [[HepG2_C3A (line)]] | wt | 198 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -20.1) |
| [[J82 (line)]] | alt | 355 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -19.4) |
| [[LS 180 (line)]] | wt | 198 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -17.0) |
| [[NCI-H1573 (line)]] | alt | 306 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -36.9) |
| [[Panc 03.27 (line)]] | alt | 299 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -32.9) |
| [[SNU-1 (line)]] | wt | 329 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -15.3) |
| [[SW 900 (line)]] | alt | 206 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -26.9) |
| [[KATO III (line)]] | alt | 261 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -25.1) |
| [[NCI-H2347 (line)]] | alt | 257 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -16.4) |
| [[RKO (line)]] | wt | 303 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 144 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -24.3) |
| [[CHP-212 (line)]] | wt | 331 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0857× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -12.2) |
| [[LoVo (line)]] | wt | 181 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -26.7) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -22.6) |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -21.7) |
| [[SW48 (line)]] | wt | 251 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.1) |
| [[A498 (line)]] | wt | 105 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -20.2) |
| [[SW1417 (line)]] | alt | 193 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -21.3) |
| [[C-33 A (line)]] | alt | 365 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.533× (z -8.9) |
| [[COLO 205 (line)]] | alt | 199 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -16.2) |
| [[HT-29 (line)]] | alt | 167 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.8) |
| [[SHP-77 (line)]] | alt | 182 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -8.5) |
| [[SW 1271 (line)]] | alt | 245 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.4) |
| [[A-427 (line)]] | wt | 313 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 314 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -15.4) |
| [[NCI-H2122 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR45B]] | +0.75 | +0.84 / +0.64 | both halves | 7e-06 |  |
| [[PDK3]] | +0.75 | +0.83 / +0.64 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.75 | +0.83 / +0.64 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[HERC3]] | +0.73 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.72 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[TBC1D9B]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.72 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[PLEKHA2]] | +0.71 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[PDK1]] | +0.70 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[ARFGEF3]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SFXN1]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | -0.55 | -0.66 / -0.37 | both halves | 8e-05 |  |
| [[AVEN]] | -0.53 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[ARHGAP42]] | -0.53 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises YEATS2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RDH10]] | B | RDH10 activity lowers YEATS2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.52× higher at baseline in the lines without RDH10 | 0.0999 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCKIPSD]] | C | YEATS2's natural level strengthens NCKIPSD's drug response | YEATS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.40; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Posaconazole (drug)]] 5 µM | C | YEATS2's natural level lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | YEATS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, -17.0); signed map (-37.5, 24.8). **Vector** length 98.3, 44.7% of its response variance represented; |z| ≥ 3 in 1,258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.0 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.9 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +5.1 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | -0.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -15.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -14.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -31.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -8.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | YEATS domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,697,797-183,812,624 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10201, FLJ12841, FLJ13308, KIAA1197 |
| Gene groups (HGNC) | ATAC complex; YEATS domain containing |
| Reactome | 6 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; HATs acetylate histones; Epigenetic regulation by WDR5-containing histone modifying complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULM3](https://www.uniprot.org/uniprotkb/Q9ULM3) (YEATS domain-containing protein 2):

> Chromatin reader component of the ATAC complex, a complex with histone acetyltransferase activity on histones H3 and H4. YEATS2 specifically recognizes and binds histone H3 crotonylated at 'Lys-27' (H3K27cr). Crotonylation marks active promoters and enhancers and confers resistance to transcriptional repressors.

**Summary**, from NCBI Gene [55689](https://www.ncbi.nlm.nih.gov/gene/55689):

> Summary: The protein encoded by this gene is a scaffolding subunit of the ATAC complex, which is a complex with acetyltransferase activity on histones H3 and H4. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:25489](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25489) · Entrez [55689](https://www.ncbi.nlm.nih.gov/gene/55689) · UniProt [Q9ULM3](https://www.uniprot.org/uniprotkb/Q9ULM3) · Ensembl [ENSG00000163872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163872)

## Data

Gene col 8797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8797); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8797]; `tensor/DDL_lfc|DDL_z.npy` [8797]; `embed/gene_vectors.npy` [8797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8797 or target_col == 8797). Every well: [[YEATS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YEATS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

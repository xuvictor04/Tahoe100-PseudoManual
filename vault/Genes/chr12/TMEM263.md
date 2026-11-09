---
symbol: "TMEM263"
type: "gene"
col: 7488
ensembl_id: "ENSG00000151135"
name: "transmembrane protein 263"
location: "12q23.3"
module: 56
arm: "+"
pooled_cpm: 181.47
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TMEM263

*transmembrane protein 263* — 12q23.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (HOP62 1.36×, MIA PaCa-2 1.28×, A498 1.19×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.486× (z -17.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG6]] (+0.88, fdr 7e-06), [[COPB1]] (+0.86, fdr 7e-06), [[PGM3]] (+0.83, fdr 7e-06); moves opposite to [[SLC25A13]] (-0.66, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 3 lines (HOP62 1.36×, MIA PaCa-2 1.28×, A498 1.19×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +8.7 | 2e-15 | 6/50 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Goserelin (acetate) (drug)]] 0.5 µM |  | 1.24× | +3.1 | 0.50 | 23/49 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.486×** | -17.5 | 0e+00 | 44/48 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.407×** | -15.6 | 0e+00 | 47/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.402×** | -15.2 | 0e+00 | 46/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.461×** | -13.5 | 4e-39 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.463×** | -13.4 | 8e-39 | 46/49 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.468×** | -13.2 | 8e-38 | 46/48 (A498, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.604×** | -12.3 | 1e-32 | 39/49 (AsPC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.493×** | -11.8 | 2e-30 | 41/44 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.511×** | -10.8 | 2e-25 | 41/45 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -10.4 | 1e-23 | 39/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.697×** | -8.8 | 6e-17 | 42/48 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -8.5 | 6e-16 | 41/47 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.621×** | -7.9 | 9e-14 | 40/48 (LoVo, NCI-H1573, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -7.9 | 1e-13 | 42/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.641×** | -7.6 | 1e-12 | 42/48 (HS-578T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.679×** | -6.7 | 6e-10 | 37/48 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -6.0 | 5e-08 | 31/48 (NCI-H1573, BT-474, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.718×** | -5.7 | 2e-07 | 33/48 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.731×** | -5.4 | 1e-06 | 30/48 (NCI-H1573, H4, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.608×** | -4.5 | 1e-04 | 30/49 (CFPAC-1, H4, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.774×** | -4.4 | 3e-04 | 26/48 (KATO III, LS 180, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.800×** | -3.9 | 0.002 | 24/48 (A549, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 269 | 0 | 17 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -26.8) |
| [[NCI-H2347 (line)]] | alt | 331 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -27.3) |
| [[HS-578T (line)]] | alt | 245 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -26.9) |
| [[hTERT-HPNE (line)]] | wt | 295 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -17.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -13.8) |
| [[LoVo (line)]] | wt | 195 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 146 | 0 | 12 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -11.3) |
| [[H4 (line)]] | wt | 294 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -19.6) |
| [[SW 900 (line)]] | alt | 304 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.495× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 209 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.3) |
| [[KATO III (line)]] | alt | 116 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -21.1) |
| [[A498 (line)]] | wt | 298 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -12.8) |
| [[SW1417 (line)]] | alt | 126 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -16.4) |
| [[A-172 (line)]] | wt | 166 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -20.4) |
| [[RPMI-7951 (line)]] | alt | 251 | 0 | 8 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.248× (z -14.9) |
| [[HCT15 (line)]] | alt | 255 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -12.2) |
| [[HOP62 (line)]] | alt | 238 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.4) |
| [[Hs 766T (line)]] | wt | 200 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 320 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.373× (z -8.7) |
| [[A549 (line)]] | wt | 175 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -12.8) |
| [[HT-29 (line)]] | alt | 118 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.400× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 202 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.5) |
| [[J82 (line)]] | alt | 182 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 197 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.9) |
| [[SNU-1 (line)]] | wt | 199 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 225 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.2) |
| [[BT-474 (line)]] | alt | 126 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.8) |
| [[COLO 205 (line)]] | alt | 155 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[Panc 03.27 (line)]] | alt | 98.9 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.140× (z -10.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.399× (z -9.2) |
| [[A-427 (line)]] | wt | 100 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.9) |
| [[SW 1088 (line)]] | alt | 295 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0923× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 102 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.0) |
| [[CHP-212 (line)]] | wt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.6) |
| [[LS 180 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.0) |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 164 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 254 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[AN3 CA (line)]] | alt | 127 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 98.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG6]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 |  |
| [[COPB1]] | +0.86 | +0.85 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[PGM3]] | +0.83 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ACBD3]] | +0.83 | +0.80 / +0.83 | both halves | 7e-06 |  |
| [[SRP54]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.82 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SEC24D]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[SUCO]] | +0.80 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[COPA]] | +0.79 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.78 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A13]] | -0.66 | -0.70 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TMEM263's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.899). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -34.8); signed map (-50.7, 12.2). **Vector** length 127, 51.1% of its response variance represented; |z| ≥ 3 in 1,432 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.72 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.74 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.74 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | -12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | -3.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +1.4 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -7.0 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -7.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.8 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.7 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -2.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.0 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 263 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:106,955,719-106,978,778 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17943; previously C12orf23 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUH6](https://www.uniprot.org/uniprotkb/Q8WUH6) (Transmembrane protein 263):

> May play a role in bone development.

**Summary**, from NCBI Gene [90488](https://www.ncbi.nlm.nih.gov/gene/90488):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28281) · Entrez [90488](https://www.ncbi.nlm.nih.gov/gene/90488) · UniProt [Q8WUH6](https://www.uniprot.org/uniprotkb/Q8WUH6) · Ensembl [ENSG00000151135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151135)

## Data

Gene col 7488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7488); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7488]; `tensor/DDL_lfc|DDL_z.npy` [7488]; `embed/gene_vectors.npy` [7488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7488 or target_col == 7488). Every well: [[TMEM263 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM263.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

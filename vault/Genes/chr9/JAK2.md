---
symbol: "JAK2"
type: "gene"
col: 1773
ensembl_id: "ENSG00000096968"
name: "Janus kinase 2"
location: "9p24.1"
module: 104
arm: "+"
pooled_cpm: 71.16
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 33
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# JAK2

*Janus kinase 2* — 9p24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 3.64×; ⚠ cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (SW 900 3.79×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 900 3.75×); [[Budesonide (drug)]] 5 µM in 1 line (SW 900 3.71×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.519× (z -10.4, q 2e-22, down in 32 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.645× (z -7.3, q 4e-11, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNA2]] (+0.53, fdr 2e-05), [[SNX7]] (+0.48, fdr 6e-05), [[LTBP1]] (+0.47, fdr 5e-05); moves opposite to [[MFSD4B]] (-0.58, fdr 2e-05), [[MIR30DHG]] (-0.49, fdr 4e-05), [[PPP1R3E]] (-0.46, fdr 5e-05).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02154]] → it (grade B ⚠); 33 go from it, the strongest it → [[TAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1773.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 3.64×; ⚠ cell-cycle shift, would explain all of this change); [[Clobetasol propionate (drug)]] 5 µM in 1 line (SW 900 3.79×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (SW 900 3.75×); [[Budesonide (drug)]] 5 µM in 1 line (SW 900 3.71×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.2 | 0.56 | 8/47 (Panc 03.27, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1773.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -10.4 | 2e-22 | 32/46 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.590×** | -8.4 | 1e-14 | 28/40 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -8.0 | 2e-13 | 28/42 (Panc 03.27, SW48, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -7.3 | 4e-11 | 34/47 (SK-MEL-2, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.677×** | -6.5 | 1e-08 | 30/47 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.791×** | -5.5 | 3e-06 | 28/47 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.731×** | -5.2 | 1e-05 | 24/47 (A498, A-172, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -5.1 | 2e-05 | 23/47 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.743×** | -4.9 | 5e-05 | 22/47 (NCI-H460, KATO III, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -4.9 | 6e-05 | 27/47 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.755×** | -4.7 | 1e-04 | 27/47 (LS 180, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.769×** | -4.4 | 5e-04 | 24/46 (KATO III, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.772×** | -4.1 | 0.002 | 24/46 (SNU-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.781×** | -4.0 | 0.003 | 26/46 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.797×** | -3.6 | 0.010 | 24/49 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.5 | 0.013 | 18/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.673×** | -3.4 | 0.018 | 17/47 (NCI-H460, NCI-H661, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.764×** | -3.2 | 0.041 | 19/45 (RKO, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.839× | -2.9 | 0.088 | 16/47 (CFPAC-1, AsPC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.714×** | -2.9 | 0.088 | 15/47 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1773. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 113 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -16.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 109 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.406× (z -9.4) |
| [[LoVo (line)]] | wt | 102 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 102 | 6 | 0 | [[Clobetasol propionate (drug)]] 5 µM 3.79× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 129 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -11.2) |
| [[A-172 (line)]] | wt | 132 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.210× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 74.1 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 122 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.482× (z -9.2) |
| [[LS 180 (line)]] | wt | 165 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 72.0 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.329× (z -10.5) |
| [[SW48 (line)]] | wt | 127 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0640× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.261× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 58.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.487× (z -9.4) |
| [[SNU-1 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -22.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 88.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -8.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -9.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0860× (z -12.0) ⚠ toxic |
| [[HS-578T (line)]] | alt | 179 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -8.9) |
| [[HT-29 (line)]] | alt | 55.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.303× (z -9.0) |
| [[J82 (line)]] | alt | 76.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0536× (z -24.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.219× (z -8.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.451× (z -9.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[AN3 CA (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1773), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNA2]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[SNX7]] | +0.48 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[LTBP1]] | +0.47 | +0.39 / +0.44 | both halves | 5e-05 |  |
| [[ITGA4]] | +0.44 | +0.43 / +0.36 | both halves | 1e-04 | pathway: Potential therapeutics for SARS |
| [[CHSY3]] | +0.44 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[STXBP5]] | +0.43 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[KLHL2]] | +0.43 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[NSMCE4A]] | +0.43 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[TMTC1]] | +0.42 | +0.32 / +0.46 | both halves | 1e-04 |  |
| [[DZIP1L]] | +0.42 | +0.39 / +0.38 | both halves | 7e-05 |  |
| [[KIF2A]] | +0.40 | +0.41 / +0.37 | both halves | 8e-05 | pathway: HALLMARK_COMPLEMENT |
| [[COBLL1]] | +0.40 | +0.45 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFSD4B]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MIR30DHG]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PPP1R3E]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TESMIN]] | -0.45 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[L3MBTL1]] | -0.44 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[C4orf47]] | -0.43 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[MMP24OS]] | -0.41 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[TMEM14B]] | -0.41 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[SPATA24]] | -0.41 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[LINC02018]] | -0.40 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[CXCL13]] | -0.40 | -0.31 / -0.43 | both halves | 2e-04 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[RINL]] | -0.40 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02154]] | B | LINC02154 activity raises JAK2's level | lines that do not express LINC02154 (37) vs lines expressing it (13) | 1.59× lower at baseline in the lines without LINC02154 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FCRLA, ENSG00000234426, ENSG00000289530 |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 33, C 0. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TAP2]] | B | JAK2 activity raises TAP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[OGFR]] | B | JAK2 activity raises OGFR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[TRIM25]] | B | JAK2 activity raises TRIM25's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[ADAR]] | B | JAK2 activity raises ADAR's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[STRIP2]] | B | JAK2 activity raises STRIP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[NAMPT]] | B | JAK2 activity raises NAMPT's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[ZSCAN5A]] | B | JAK2 activity lowers ZSCAN5A's level | compounds that target JAK2: 2 of 3 raise it (Fedratinib, Filgotinib) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[IL15]] | B | JAK2 activity raises IL15's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[PATL1]] | B | JAK2 activity raises PATL1's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[TRAF3IP2]] | B | JAK2 activity raises TRAF3IP2's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[IL15RA]] | B | JAK2 activity raises IL15RA's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PLEKHA4]] | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.397). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.8, 8.6); signed map (21.2, 36.4). **Vector** length 93.1, 23.0% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +2.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +2.5 | -4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | -0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.6 | -5.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -7.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.5 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | Janus kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:4,984,390-5,129,948 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JTK10 |
| Gene groups (HGNC) | SH2 domain containing; FERM domain containing; Jak family tyrosine kinases |
| Hallmark sets | ALLOGRAFT_REJECTION, COMPLEMENT, INTERFERON_GAMMA_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 66 pathways, smallest: Erythropoietin activates Phospholipase C gamma (PLCG); Erythropoietin activates STAT5; Interleukin-23 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O60674](https://www.uniprot.org/uniprotkb/O60674) (Tyrosine-protein kinase JAK2):

> Non-membrane spanning protein tyrosine kinase that phosphorylates type I receptors such as growth hormone (GHR), prolactin (PRLR), leptin (LEPR), erythropoietin (EPOR), thrombopoietin receptor (MPL/TPOR); or type II receptors including IFN-alpha, IFN-beta, IFN-gamma and multiple interleukins. Functionally, plays a pivotal role in signal transduction and is involved in various processes such as cell growth, development, differentiation or histone modifications. Mediates essential signaling …

**Summary**, from NCBI Gene [3717](https://www.ncbi.nlm.nih.gov/gene/3717):

> This gene encodes a non-receptor tyrosine kinase that plays a central role in cytokine and growth factor signalling. The primary isoform of this protein has an N-terminal FERM domain that is required for erythropoietin receptor association, an SH2 domain that binds STAT transcription factors, a pseudokinase domain and a C-terminal tyrosine kinase domain. Cytokine binding induces autophosphorylation and activation of this kinase. This kinase then recruits and phosphorylates signal transducer and …

**Accessions** — [HGNC:6192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6192) · Entrez [3717](https://www.ncbi.nlm.nih.gov/gene/3717) · UniProt [O60674](https://www.uniprot.org/uniprotkb/O60674) · Ensembl [ENSG00000096968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096968)

## Data

Gene col 1773: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1773); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1773, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1773]; `tensor/DDL_lfc|DDL_z.npy` [1773]; `embed/gene_vectors.npy` [1773]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1773 or target_col == 1773). Every well: [[JAK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

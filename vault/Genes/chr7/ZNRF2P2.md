---
symbol: "ZNRF2P2"
type: "gene"
col: 13445
ensembl_id: "ENSG00000225264"
name: "zinc and ring finger 2 pseudogene 2"
location: "7p14.3"
module: 18
arm: "+"
pooled_cpm: 37.65
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ZNRF2P2

*zinc and ring finger 2 pseudogene 2* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +7.8, q 3e-12, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.548× (z -15.9, q 0e+00, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNRF2P1]] (+0.83, fdr 7e-06), [[DPY19L2P3]] (+0.71, fdr 7e-06, ⚠ same locus), [[NRF1]] (+0.67, fdr 7e-06), [[PKD2]] (+0.61, fdr 1e-05); moves opposite to [[MKNK1]] (-0.54, fdr 4e-05), [[CLTC]] (-0.53, fdr 5e-05), [[CDC37]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13445.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.8 | 3e-12 | 27/46 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 2e-04 | 23/45 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.053 | 20/45 (H4, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.069 | 18/45 (RPMI-7951, H4, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.13× | +3.4 | 0.069 | 7/46 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.3 | 0.10 | 15/45 (HT-29, SW480, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.0 | 0.18 | 12/45 (LS 180, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13445.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.548×** | -15.9 | 0e+00 | 33/46 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.530×** | -11.5 | 3e-28 | 27/38 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.546×** | -11.4 | 6e-28 | 33/46 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.578×** | -10.3 | 7e-23 | 28/42 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.597×** | -9.7 | 3e-20 | 33/46 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.626×** | -8.8 | 1e-16 | 32/45 (SW480, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.652×** | -7.7 | 9e-13 | 27/46 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.686×** | -7.1 | 9e-11 | 33/46 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.680×** | -6.7 | 1e-09 | 24/41 (NCI-H1573, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -5.7 | 8e-07 | 24/47 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.753×** | -5.3 | 5e-06 | 22/44 (H4, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.758×** | -5.2 | 9e-06 | 20/45 (SHP-77, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.603×** | -5.0 | 3e-05 | 23/46 (SW480, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.771×** | -4.7 | 1e-04 | 22/45 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.6 | 2e-04 | 3/46 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.766×** | -3.6 | 0.012 | 10/46 (SW480, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.710×** | -3.4 | 0.025 | 8/45 (SW1417, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.786×** | -3.2 | 0.040 | 10/46 (COLO 205, SW1417, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.836× | -3.2 | 0.047 | 18/46 (SW480, Hs 766T, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.739×** | -3.0 | 0.082 | 12/45 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.089 | 12/45 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.089 | 9/45 (SW480, C32, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -2.9 | 0.089 | 15/46 (A-172, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13445. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 55.8 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -15.5) |
| [[C32 (line)]] | wt | 57.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -24.0) |
| [[PANC-1 (line)]] | alt | 78.9 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.474× (z -13.0) |
| [[A-172 (line)]] | wt | 32.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -22.3) |
| [[NCI-H460 (line)]] | wt | 46.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -15.5) |
| [[A498 (line)]] | wt | 36.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.5) |
| [[SHP-77 (line)]] | alt | 93.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -13.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.441× (z -8.8) |
| [[SW1417 (line)]] | alt | 72.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.8) |
| [[SW480 (line)]] | alt | 43.5 | 0 | 5 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.339× (z -13.2) |
| [[C-33 A (line)]] | alt | 64.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 42.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.8) |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0757× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.138× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 74.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.4) |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 26.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 44.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.5) |
| [[RKO (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -11.8) |
| [[A-427 (line)]] | wt | 45.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 39.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.1) |
| [[AN3 CA (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.6) |
| [[H4 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0805× (z -14.7) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.105× (z -9.1) ⚠ toxic |
| [[NCI-H661 (line)]] | alt | 45.7 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0757× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 27.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0541× (z -8.8) |
| [[SW48 (line)]] | wt | 43.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.129× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.25 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13445), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNRF2P1]] | +0.83 | +0.85 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[DPY19L2P3]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[NRF1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[PKD2]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[DPY19L1P1]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[C2orf69]] | +0.60 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SLC49A4]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB44]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[AGO4]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CRTC3]] | +0.57 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[MTFMT]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ARID2]] | +0.55 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKNK1]] | -0.54 | -0.50 / -0.43 | both halves | 4e-05 |  |
| [[CLTC]] | -0.53 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[CDC37]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TTN-AS1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SYAP1]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[UBE4A]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CREB3]] | -0.48 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PDPK1]] | -0.48 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[CLIC1]] | -0.48 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[AP3D1]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[INTS3]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[HAPSTR1]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity lowers ZNRF2P2's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.87× higher at baseline in the lines without F3 | 0.006 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[F3]] | B | F3 activity weakens ZNRF2P2's drug response | lines that do not express F3 (24) vs lines expressing it (22) | the lines without F3 respond 1.71× as strongly (z diff -2.24); strongest at Dinaciclib 0.5 µM: 0.38x vs 0.80x (z diff -5.2) | 0.006 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA; target measured in part of the lines; artifact flags |
| [[HOXC8]] | B | HOXC8 activity raises ZNRF2P2's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without HOXC8 | 0.037 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.7, 13.8); signed map (7.3, -4.8). **Vector** length 112, 28.5% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.3 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.2 | +3.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.9 | +5.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.3 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -4.3 | -10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -8.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.9 | -11.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[EX229 (drug)]] 0.05 µM |  | -2.3 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc and ring finger 2 pseudogene 2 |
| Locus type | pseudogene |
| Location | 7p14.3 — chr7:29,684,773-29,685,192 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:42793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42793) · Entrez [100271874](https://www.ncbi.nlm.nih.gov/gene/100271874) · Ensembl [ENSG00000225264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225264)

## Data

Gene col 13445: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13445); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13445, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13445]; `tensor/DDL_lfc|DDL_z.npy` [13445]; `embed/gene_vectors.npy` [13445]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13445 or target_col == 13445). Every well: [[ZNRF2P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRF2P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

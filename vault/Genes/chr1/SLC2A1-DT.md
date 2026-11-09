---
symbol: "SLC2A1-DT"
type: "gene"
col: 13598
ensembl_id: "ENSG00000227533"
name: "SLC2A1 divergent transcript"
location: "1p34.2"
module: 105
arm: "+"
pooled_cpm: 25.41
n_lines_expressing: 47
n_dd_up: 8
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# SLC2A1-DT

*SLC2A1 divergent transcript* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +10.0, q 8e-21, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.298× (z -29.0, q 0e+00, down in 42 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNMT]] (+0.66, fdr 7e-06), [[INSIG2]] (+0.65, fdr 7e-06), [[ANKRD37]] (+0.64, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.64, fdr 1e-05), [[ZNF644]] (-0.53, fdr 1e-05), [[SMARCD1]] (-0.53, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HLA-V-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +10.0 | 8e-21 | 28/43 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +9.3 | 4e-18 | 30/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +7.4 | 4e-11 | 25/45 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +7.2 | 1e-10 | 27/41 (A-172, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 3e-05 | 16/45 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 2e-04 | 13/45 (HOP62, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.004 | 14/45 (A-172, A-427, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.082 | 4/43 (HS-578T, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.298×** | -29.0 | 0e+00 | 42/43 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.263×** | -21.8 | 0e+00 | 42/44 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -18.7 | 0e+00 | 37/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.341×** | -17.6 | 0e+00 | 37/40 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.376×** | -16.6 | 0e+00 | 39/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -13.8 | 2e-41 | 32/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.449×** | -13.6 | 5e-40 | 34/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.491×** | -12.1 | 1e-31 | 34/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.303×** | -10.6 | 2e-24 | 33/43 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.306×** | -10.5 | 6e-24 | 30/44 (HT-29, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.579×** | -9.3 | 1e-18 | 26/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -8.7 | 1e-16 | 27/44 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.618×** | -8.2 | 1e-14 | 22/39 (H4, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.618×** | -7.9 | 2e-13 | 28/45 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.420×** | -7.7 | 5e-13 | 17/35 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -7.7 | 6e-13 | 27/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -6.3 | 9e-09 | 23/44 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -6.2 | 2e-08 | 23/43 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.525×** | -5.7 | 3e-07 | 23/43 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 84.7 | 0 | 21 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -35.8) |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -25.1) |
| [[PANC-1 (line)]] | alt | 16.9 | 1 | 11 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -23.9) |
| [[HT-29 (line)]] | alt | 56.3 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -19.3) |
| [[H4 (line)]] | wt | 64.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0570× (z -25.5) |
| [[NCI-H1573 (line)]] | alt | 49.0 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -19.5) |
| [[COLO 205 (line)]] | alt | 62.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.180× (z -11.4) |
| [[Hs 766T (line)]] | wt | 67.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -24.1) |
| [[A549 (line)]] | wt | 13.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0878× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0464× (z -15.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -9.2) |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.225× (z -9.8) |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.0) |
| [[C32 (line)]] | wt | 17.4 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0477× (z -16.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.214× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 44.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -12.6) |
| [[KATO III (line)]] | alt | 53.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.396× (z -10.9) |
| [[LoVo (line)]] | wt | 11.3 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -11.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.226× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 16.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -24.0) |
| [[A498 (line)]] | wt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0832× (z -13.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -9.1) |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0379× (z -17.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.221× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0900× (z -9.7) |
| [[HOP62 (line)]] | alt | 13.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.197× (z -9.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 13.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -9.8) |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 8.96 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.92× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.0667× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.233× (z -9.1) |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0547× (z -13.7) |
| [[SW48 (line)]] | wt | 53.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.4) |
| [[BT-474 (line)]] | alt | 28.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -12.7) |
| [[HS-578T (line)]] | alt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +10.8) | — |
| [[J82 (line)]] | alt | 7.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0985× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H2122 (line)]] | alt | 27.2 | 1 | 0 | [[Tubulin inhibitor 6 (drug)]] 0.5 µM 1.58× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.7) |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0746× (z -8.7) |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.2) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNMT]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.65 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[EFCAB3P1]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.63 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[LINC00887]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 | same gene group |
| [[FUT11]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[HLA-F-AS1]] | +0.60 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[C4orf47]] | +0.60 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.59 | +0.57 / +0.63 | both halves | 9e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.64 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[SMARCD1]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[EXOSC10]] | -0.52 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[SLC25A24]] | -0.52 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[COA7]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PARVA]] | -0.52 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SMARCB1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[BCL7B]] | -0.51 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ZNF236]] | -0.51 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[EPC2]] | -0.51 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ZC3H14]] | -0.51 | -0.40 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-V-1]] | B | HLA-V-1 activity raises SLC2A1-DT's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without HLA-V-1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[LINC00887]] | B | LINC00887 activity raises SLC2A1-DT's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without LINC00887 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[LINC02036]] | B | LINC02036 activity raises SLC2A1-DT's level | lines that do not express LINC02036 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without LINC02036 | 0.051 | ⚠ within organs, on part of the lines; also absent: LINC00887, ENSG00000256982, SIPA1L2; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SLC2A1-DT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, -18.5); signed map (-34.3, 25.7). **Vector** length 96.4, 24.9% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +4.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.1 | -17.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -21.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -18.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.8 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -5.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | SLC2A1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p34.2 — chr1:42,959,049-42,996,814 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously SLC2A1-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44187) · Entrez [440584](https://www.ncbi.nlm.nih.gov/gene/440584) · Ensembl [ENSG00000227533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227533)

## Data

Gene col 13598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13598); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13598]; `tensor/DDL_lfc|DDL_z.npy` [13598]; `embed/gene_vectors.npy` [13598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13598 or target_col == 13598). Every well: [[SLC2A1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC2A1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

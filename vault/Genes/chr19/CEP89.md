---
symbol: "CEP89"
type: "gene"
col: 4264
ensembl_id: "ENSG00000121289"
name: "centrosomal protein 89"
location: "19q13.11"
module: 54
arm: "+"
pooled_cpm: 50.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# CEP89

*centrosomal protein 89* — 19q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.45× (z +10.3, q 5e-22, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.698× (z -14.0, q 7e-42, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DZANK1]] (+0.73, fdr 7e-06), [[ZNF487]] (+0.56, fdr 3e-05), [[NBPF12]] (+0.55, fdr 2e-05); moves opposite to [[NTRK3]] (-0.54, fdr 6e-05), [[B3GALT1]] (-0.48, fdr 3e-05), [[THBS1]] (-0.47, fdr 5e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4264.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +10.3 | 5e-22 | 27/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +7.7 | 5e-12 | 24/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +7.0 | 5e-10 | 24/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.23×** | +5.4 | 7e-06 | 19/48 (SW48, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +5.0 | 6e-05 | 16/48 (HepG2/C3A, J82, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +4.9 | 1e-04 | 17/48 (SW1417, PANC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +4.8 | 1e-04 | 13/48 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.19× | +4.7 | 1e-04 | 17/48 (J82, AsPC-1, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +4.0 | 0.005 | 6/48 (AsPC-1, RKO, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.006 | 10/48 (A498, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +3.6 | 0.017 | 12/47 (H4, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.14× | +3.5 | 0.017 | 12/48 (SW48, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.017 | 10/48 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.13× | +3.5 | 0.017 | 9/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.5 | 0.017 | 16/48 (SHP-77, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4264.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.698×** | -14.0 | 7e-42 | 41/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.696×** | -10.0 | 5e-21 | 35/48 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.719×** | -8.4 | 1e-14 | 29/43 (A-172, LS 180, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -7.7 | 2e-12 | 30/48 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.734×** | -6.3 | 2e-08 | 22/47 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.745×** | -6.1 | 1e-07 | 20/48 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.811×** | -5.7 | 7e-07 | 22/45 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.813×** | -5.7 | 9e-07 | 24/48 (BT-474, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **0.822×** | -5.4 | 5e-06 | 21/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.879× | -5.0 | 3e-05 | 19/48 (A-172, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.836× | -4.9 | 5e-05 | 20/48 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.853× | -4.4 | 6e-04 | 22/48 (SW480, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.881× | -3.5 | 0.023 | 10/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.882× | -3.4 | 0.023 | 18/48 (BT-474, SW480, …) | rises with dose |  |
| [[Ritonavir (drug)]] 0.05 µM |  | 0.895× | -3.0 | 0.097 | 4/48 (CFPAC-1, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4264. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 94.4 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.493× (z -13.6) |
| [[HS-578T (line)]] | alt | 95.7 | 0 | 3 (2 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.570× (z -9.6) |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.474× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 41.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.390× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 67.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -12.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.519× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 29.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 69.3 | 0 | 2 | — | [[Tucidinostat (drug)]] 0.5 µM 0.295× (z -11.8) |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.379× (z -10.3) |
| [[A-427 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 95.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 87.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.471× (z -10.3) |
| [[HOP62 (line)]] | alt | 96.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.582× (z -10.1) |
| [[J82 (line)]] | alt | 60.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 40.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 41.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.98× (z +9.5) | — |
| [[A498 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4264), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | +0.73 | +0.60 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ZNF487]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[NBPF12]] | +0.55 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[SMG6]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HECTD4]] | +0.54 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[VRK3]] | +0.53 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TCTN2]] | +0.52 | +0.51 / +0.50 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[GLE1]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ZNF765]] | +0.51 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PMM1]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SMYD4]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[KATNIP]] | +0.50 | +0.39 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NTRK3]] | -0.54 | -0.39 / -0.59 | both halves | 6e-05 |  |
| [[B3GALT1]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[THBS1]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[GLRB]] | -0.46 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[PON2]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[PLXDC2]] | -0.45 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[PDLIM3]] | -0.45 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[MOXD1]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[MED12L]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[GPM6A]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TLCD4]] | -0.44 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[PEG10]] | -0.43 | -0.44 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CEP89's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.244). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.1, 22.6); signed map (-19.0, 3.4). **Vector** length 108, 26.1% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +4.0 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +10.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | +3.9 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +7.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -11.5 | -14.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.8 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.8 | -8.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 89 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.11 — chr19:32,875,925-32,971,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14640; previously CCDC123 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96ST8](https://www.uniprot.org/uniprotkb/Q96ST8) (Centrosomal protein of 89 kDa):

> Required for ciliogenesis. Also plays a role in mitochondrial metabolism where it may modulate complex IV activity.

**Summary**, from NCBI Gene [84902](https://www.ncbi.nlm.nih.gov/gene/84902):

> Involved in mitochondrial respiratory chain complex IV assembly and non-motile cilium assembly. Acts upstream of or within cilium assembly. Located in several cellular components, including microtubule cytoskeleton; mitochondrial intermembrane space; and non-motile cilium. Part of ciliary transition fiber. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25907) · Entrez [84902](https://www.ncbi.nlm.nih.gov/gene/84902) · UniProt [Q96ST8](https://www.uniprot.org/uniprotkb/Q96ST8) · Ensembl [ENSG00000121289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121289)

## Data

Gene col 4264: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4264); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4264, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4264]; `tensor/DDL_lfc|DDL_z.npy` [4264]; `embed/gene_vectors.npy` [4264]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4264 or target_col == 4264). Every well: [[CEP89 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP89.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

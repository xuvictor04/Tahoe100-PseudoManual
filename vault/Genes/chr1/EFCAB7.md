---
symbol: "EFCAB7"
type: "gene"
col: 12804
ensembl_id: "ENSG00000203965"
name: "EF-hand calcium binding domain 7"
location: "1p31.3"
module: 64
arm: "+"
pooled_cpm: 12.17
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 19
n_dd_up_clean: 26
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# EFCAB7

*EF-hand calcium binding domain 7* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (8 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.03× (z +11.5, q 1e-27, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.607× (z -8.6, q 6e-15, down in 25 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTU]] (+0.78, fdr 7e-06), [[DYNC2LI1]] (+0.76, fdr 7e-06), [[TMLHE]] (+0.74, fdr 7e-06); moves opposite to [[LINC01128]] (-0.59, fdr 7e-06), [[CFL1]] (-0.59, fdr 2e-05), [[KLF13]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ANKEF1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.03×** | +11.5 | 1e-27 | 34/46 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.85×** | +10.6 | 9e-24 | 31/47 (HOP62, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +10.5 | 1e-23 | 33/47 (HOP62, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.49×** | +9.7 | 5e-20 | 32/48 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.72×** | +9.4 | 9e-19 | 32/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +8.4 | 4e-15 | 34/48 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +7.1 | 1e-10 | 22/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +6.8 | 6e-10 | 19/47 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +6.7 | 1e-09 | 22/45 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.5 | 3e-09 | 23/47 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.46×** | +6.5 | 3e-09 | 19/47 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +6.3 | 2e-08 | 21/47 (RKO, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.35×** | +5.2 | 7e-06 | 14/47 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 4e-05 | 13/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.34×** | +4.8 | 5e-05 | 16/41 (C32, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.8 | 6e-05 | 15/47 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.32×** | +4.8 | 6e-05 | 11/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 6e-05 | 11/48 (BT-474, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.69×** | +4.7 | 8e-05 | 14/43 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12804.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.607×** | -8.6 | 6e-15 | 25/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -8.3 | 3e-14 | 26/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.630×** | -7.9 | 4e-13 | 23/46 (J82, HCT15, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -7.9 | 6e-13 | 23/46 (H4, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.638×** | -7.7 | 1e-12 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -6.4 | 1e-08 | 21/39 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.707×** | -5.9 | 2e-07 | 20/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.792×** | -5.7 | 1e-06 | 21/48 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.746×** | -5.0 | 3e-05 | 14/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -4.9 | 5e-05 | 15/47 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.752×** | -4.9 | 5e-05 | 20/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.686×** | -4.6 | 2e-04 | 15/44 (HCT15, SW 900, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.761×** | -4.5 | 3e-04 | 16/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.3 | 7e-04 | 15/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.784×** | -4.2 | 0.001 | 16/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.792×** | -4.0 | 0.002 | 17/44 (CFPAC-1, SNU-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.668×** | -3.6 | 0.010 | 13/40 (C-33 A, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.012 | 5/48 (PANC-1, SW480, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.677×** | -3.5 | 0.014 | 9/44 (Hs 766T, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.885× | -3.0 | 0.080 | 12/48 (Hs 766T, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 16.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.41× (z +18.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 8.20 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0655× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Orlistat (drug)]] 0.05 µM 0.150× (z -9.3) |
| [[A-427 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.345× (z -9.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HOP62 (line)]] | alt | 8.54 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.86× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.261× (z -9.3) |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.354× (z -8.5) |
| [[RKO (line)]] | wt | 10.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.5× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 22.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.317× (z -11.0) |
| [[A-172 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTU]] | +0.78 | +0.79 / +0.75 | both halves | 7e-06 | pathway: Signaling by Hedgehog |
| [[DYNC2LI1]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.74 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PIGB]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[APOOL]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[PSMC1]] | +0.67 | +0.63 / +0.58 | both halves | 7e-06 | pathway: Hedgehog 'on' state |
| [[GNPDA2]] | +0.66 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[CWF19L2]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[CDC40]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[RBM41]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[USP30]] | +0.64 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01128]] | -0.59 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[CFL1]] | -0.59 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[KLF13]] | -0.56 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[DUSP7]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MAMLD1]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MYL12A]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CD9]] | -0.53 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises EFCAB7's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without ZNF675 | 0.049 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[NRG4]] | B | NRG4 activity raises EFCAB7's level | lines that do not express NRG4 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without NRG4 | 0.057 | ⚠ within organs, on part of the lines; also absent: LHFPL6, ENSG00000288583; maybe low, not absent |
| [[BBS5]] | B | BBS5 activity raises EFCAB7's level | lines that do not express BBS5 (6) vs lines expressing it (44) | 1.34× lower at baseline in the lines without BBS5 | 0.062 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, FERMT2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKEF1]] | C | EFCAB7's natural level strengthens ANKEF1's drug response | EFCAB7's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.09; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.5, -0.1); signed map (-21.0, -21.2). **Vector** length 84.9, 16.8% of its response variance represented; |z| ≥ 3 in 1,099 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.4 | +10.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.2 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +8.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.7 | +6.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -6.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:63,523,372-63,572,693 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1799, RP4-534K7.1 |
| Gene groups (HGNC) | EF-hand domain containing; EvC complex subunits |
| Reactome | 3 pathways, smallest: Activation of SMO; Hedgehog 'on' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [A8K855](https://www.uniprot.org/uniprotkb/A8K855) (EF-hand calcium-binding domain-containing protein 7):

> Component of the EvC complex that positively regulates ciliary Hedgehog (Hh) signaling. Required for the localization of the EVC2:EVC subcomplex at the base of primary cilia.

**Summary**, from NCBI Gene [84455](https://www.ncbi.nlm.nih.gov/gene/84455):

> Predicted to enable calcium ion binding activity. Predicted to be involved in positive regulation of protein import into nucleus; positive regulation of protein localization to ciliary membrane; and positive regulation of transcription by RNA polymerase II. Predicted to be located in cytoplasmic side of plasma membrane. Predicted to be part of plasma membrane protein complex. Predicted to be active in ciliary membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29379) · Entrez [84455](https://www.ncbi.nlm.nih.gov/gene/84455) · UniProt [A8K855](https://www.uniprot.org/uniprotkb/A8K855) · Ensembl [ENSG00000203965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203965)

## Data

Gene col 12804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12804); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12804]; `tensor/DDL_lfc|DDL_z.npy` [12804]; `embed/gene_vectors.npy` [12804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12804 or target_col == 12804). Every well: [[EFCAB7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SMAD6"
type: "gene"
col: 6082
ensembl_id: "ENSG00000137834"
name: "SMAD family member 6"
location: "15q22.31"
module: 29
arm: "+"
pooled_cpm: 26.14
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029", "written"]
generated_by: "tahoemap"
---

# SMAD6

*SMAD family member 6* — 15q22.31

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> SMAD6 is an inhibitory SMAD: a BMP-induced brake that blocks signalling through its own pathway rather than transmitting it.

## What it is

SMAD6 and SMAD7 lack the C-terminal SSXS motif that makes receptor SMADs phosphorylation substrates, and work as antagonists. SMAD6 acts mainly on the BMP branch: it competes with [[SMAD4]] for binding to activated SMAD1, and recruits the ubiquitin ligase SMURF1 to receptors and SMADs. It is a BMP target gene, which closes a negative-feedback loop. A nuclear repressor role is also reported, with MH1-like DNA binding and recruitment of CtBP and histone deacetylases. Smad6-null mice have valve and outflow-tract defects, and rare human loss-of-function variants are associated with craniosynostosis and bicuspid aortic valve.

## What is uncertain

SMAD6 is a weak case for regulon-based inference. It is not a classical sequence-specific activator; its direct DNA binding is reported in few systems, and most of its output is indirect, through sequestration and degradation. The curated target set is small and its signs are inherited from BMP-response experiments, so the inferred activity is as likely to report BMP tone as SMAD6.

## References

- Imamura et al., 1997, Nature — identified Smad6 as an inhibitor of signalling by the TGF-beta superfamily.
- Hata et al., 1998, Genes & Development — Smad6 inhibits BMP/Smad1 signalling by competing with SMAD4.
- Galvin et al., 2000, Nature Genetics — Smad6-null mice show cardiovascular developmental defects.
- Timberlake et al., 2016, eLife — rare SMAD6 loss-of-function variants with a common BMP2 risk allele in midline craniosynostosis.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.76× (z +4.7, q 0.001, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.365× (z -11.8, q 2e-29, down in 36 of 44 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.256× (z -11.3, q 4e-27, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRP5]] (+0.61, fdr 1e-05), [[NFIA]] (+0.60, fdr 1e-05), [[USP6NL]] (+0.58, fdr 2e-05); moves opposite to [[TBRG1]] (-0.60, fdr 3e-05), [[NIT1]] (-0.54, fdr 3e-05), [[ZCCHC9]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NUP210]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF704]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6082.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.76×** | +4.7 | 0.001 | 27/44 (J82, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +3.9 | 0.016 | 23/44 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.016 | 20/43 (A549, NCI-H1573, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.57×** | +3.8 | 0.021 | 18/43 (PANC-1, C-33 A, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.058 | 20/44 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.05 µM |  | **1.50×** | +3.4 | 0.071 | 17/44 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.32×** | +3.3 | 0.078 | 19/44 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | 1.51× | +3.2 | 0.10 | 12/43 (SW1417, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.49× | +3.1 | 0.11 | 21/43 (SW480, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.43× | +3.0 | 0.14 | 14/43 (A549, J82, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 1.31× | +3.0 | 0.14 | 17/44 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6082.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.365×** | -11.8 | 2e-29 | 36/44 (SNU-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.256×** | -11.3 | 4e-27 | 42/44 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.269×** | -10.9 | 2e-25 | 38/44 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.282×** | -10.1 | 9e-22 | 41/44 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.307×** | -9.8 | 1e-20 | 33/43 (BT-474, A-427, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.327×** | -9.3 | 2e-18 | 37/43 (HEC-1-A, NCI-H460, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.333×** | -9.1 | 7e-18 | 38/42 (SNU-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.383×** | -8.0 | 1e-13 | 34/43 (COLO 205, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.280×** | -7.6 | 1e-12 | 38/44 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.388×** | -7.4 | 7e-12 | 33/44 (COLO 205, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.545×** | -7.1 | 6e-11 | 38/44 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.430×** | -7.0 | 1e-10 | 31/43 (A-427, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.437×** | -6.9 | 3e-10 | 32/43 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.502×** | -5.5 | 2e-06 | 26/43 (A-427, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.528×** | -5.3 | 5e-06 | 27/44 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.555×** | -4.9 | 4e-05 | 33/43 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.361×** | -4.4 | 3e-04 | 23/44 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.493×** | -4.2 | 6e-04 | 22/43 (Panc 03.27, COLO 205, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 140 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0261× (z -23.6) |
| [[COLO 205 (line)]] | alt | 41.4 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0333× (z -17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0822× (z -13.3) |
| [[C-33 A (line)]] | alt | 111 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0583× (z -15.2) |
| [[PANC-1 (line)]] | alt | 35.6 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -18.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0728× (z -15.3) |
| [[A-427 (line)]] | wt | 29.4 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0874× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 34.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0370× (z -16.1) |
| [[Hs 766T (line)]] | wt | 32.0 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0592× (z -12.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -9.8) |
| [[A549 (line)]] | wt | 32.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0864× (z -18.6) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0641× (z -14.8) |
| [[SW480 (line)]] | alt | 47.4 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 27.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.0) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0951× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 14.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.52× (z +13.4) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0368× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0642× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 64.1 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -10.2) |
| [[KATO III (line)]] | alt | 31.6 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -10.8) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0590× (z -12.2) |
| [[A498 (line)]] | wt | 23.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.189× (z -9.8) |
| [[C32 (line)]] | wt | 10.1 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0430× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 25.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -9.9) |
| [[HT-29 (line)]] | alt | 77.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -15.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.206× (z -10.3) |
| [[LoVo (line)]] | wt | 25.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 8.90 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.49× (z +11.7) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -10.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.5) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.135× (z -10.5) |
| [[BT-474 (line)]] | alt | 9.31 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0415× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0364× (z -9.8) |
| [[AN3 CA (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP5]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[NFIA]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[USP6NL]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[STT3B]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MIRLET7BHG]] | +0.56 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[RAI1]] | +0.55 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TMEM123]] | +0.54 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[LRP6]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[GTF2I]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CTDSPL]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[GSE1]] | +0.52 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TNRC18]] | +0.51 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBRG1]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[NIT1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ZCCHC9]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[DYNC1I2]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[DNAJB2]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ADPRM]] | -0.50 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[KRBOX4]] | -0.50 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[C9orf72]] | -0.49 | -0.49 / -0.40 | both halves | 4e-05 |  |
| [[CSGALNACT2]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[MED10]] | -0.49 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[PPP1R21]] | -0.49 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF674]] | -0.49 | -0.43 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUP210]] | B | NUP210 activity raises SMAD6's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without NUP210 | 0.054 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF704]] | C | SMAD6 activity raises ZNF704's level | lines that do not express SMAD6 (4) vs lines expressing it (46) | 1.18× lower at baseline in the lines without SMAD6 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with NF1, B2M; also absent: ENSG00000235450; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-4.9, 39.9); signed map (29.1, -37.2). **Vector** length 84.7, 21.3% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.1 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +4.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -11.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.9 | -5.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.7 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -7.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | SMAD family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:66,702,236-66,782,849 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT17432; previously MADH7, MADH6 |
| Gene groups (HGNC) | SMAD family |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 4 pathways, smallest: RUNX2 regulates bone development; Signaling by BMP; Transcriptional regulation by RUNX2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O43541](https://www.uniprot.org/uniprotkb/O43541) (SMAD family member 6):

> Acts as an inhibitory regulator of signaling mediated by the TGF-beta superfamily, with strong selectivity toward BMP-dependent pathways. Suppresses IL1R-TLR signaling through its direct interaction with PEL1, preventing NF-kappa-B activation, nuclear translocation and NF-kappa-B-mediated expression of pro-inflammatory genes. Blocks the BMP-SMAD1 signaling pathway by competing with SMAD4 for receptor-activated SMAD1-binding. Associates with regulatory elements in target promoter regions. …

**Summary**, from NCBI Gene [4091](https://www.ncbi.nlm.nih.gov/gene/4091):

> The protein encoded by this gene belongs to the SMAD family of proteins, which are related to Drosophila 'mothers against decapentaplegic' (Mad) and C. elegans Sma. SMAD proteins are signal transducers and transcriptional modulators that mediate multiple signaling pathways. This protein functions in the negative regulation of BMP and TGF-beta/activin-signalling. Multiple transcript variants have been found for this gene.[provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:6772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6772) · Entrez [4091](https://www.ncbi.nlm.nih.gov/gene/4091) · UniProt [O43541](https://www.uniprot.org/uniprotkb/O43541) · Ensembl [ENSG00000137834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137834)

## Data

Gene col 6082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6082); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6082]; `tensor/DDL_lfc|DDL_z.npy` [6082]; `embed/gene_vectors.npy` [6082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6082 or target_col == 6082). Every well: [[SMAD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/SMAD6.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

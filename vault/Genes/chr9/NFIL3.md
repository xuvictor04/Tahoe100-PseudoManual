---
symbol: "NFIL3"
type: "gene"
col: 9056
ensembl_id: "ENSG00000165030"
name: "nuclear factor, interleukin 3 regulated"
location: "9q22.31"
module: 139
arm: "+"
pooled_cpm: 37.03
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/139", "written"]
generated_by: "tahoemap"
---

# NFIL3

*nuclear factor, interleukin 3 regulated* — 9q22.31

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> NFIL3 encodes E4BP4, a bZIP transcription factor that represses D-box promoter elements by competing with the PAR-family activators for the same sites.

## What it is

NFIL3 belongs to the proline- and acidic-amino-acid-rich (PAR) branch of the bZIP family but lacks the PAR activation domain its relatives carry, so it binds the shared D-box consensus and represses rather than activates. Its abundance oscillates in antiphase to DBP, HLF and TEF, and that competition is part of the circadian oscillator, with PER1 and PER2 among the repressed targets. It was isolated twice under different names — as E4BP4, a repressor of the adenovirus E4 promoter, and as an interleukin-3-regulated factor in haematopoietic survival. Its best-established requirement is developmental: Nfil3-deficient mice lack mature natural killer cells, and the factor acts early in the innate lymphoid lineage.

## What is uncertain

Its regulon here is small, and its targets were curated largely from circadian and mouse lymphoid systems rather than epithelial tumour cells, so coherent movement need not report NFIL3. Because it represses, the direction of its inferred activity depends on sign conventions applied inconsistently to repressors. And unsynchronised proliferating cultures have scrambled circadian phase, removing the context in which D-box coherence is interpretable.

## References

- Cowell et al., 1992, Molecular and Cellular Biology — identified E4BP4 as a bZIP transcriptional repressor.
- Mitsui et al., 2001, Genes & Development — showed E4BP4 and the PAR activators act antagonistically at D-boxes in the circadian oscillator.
- Gascoyne et al., 2009, Nature Immunology — E4BP4 is essential for natural killer cell development.
- Kamizono et al., 2009, Journal of Experimental Medicine — Nfil3/E4bp4 is required for NK cell development and maturation in vivo.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 15.1× (z +20.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.580× (z -7.0, q 2e-09, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tofacitinib (drug)]] 5 µM: 0.804× (z -4.5, q 0.001, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 0.106×, NCI-H2030 0.0587×, NCI-H2347 0.158×, NCI-H1792 0.106×, …; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (CFPAC-1 0.128×, NCI-H2347 0.253×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.166×, RKO 0.252×; ⚠ cell-cycle shift, explains ~0% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.0934×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAMPT]] (+0.72, fdr 7e-06), [[AVPI1]] (+0.68, fdr 7e-06), [[BCL6]] (+0.62, fdr 7e-06); moves opposite to [[NIPAL1]] (-0.53, fdr 3e-05), [[DCTD]] (-0.52, fdr 6e-05), [[SH3D19]] (-0.50, fdr 3e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CA12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **15.1×** | +20.4 | 0e+00 | 48/48 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.9 | 1e-09 | 26/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +6.7 | 5e-09 | 31/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +6.0 | 3e-07 | 30/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.9 | 4e-07 | 28/47 (SW480, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +5.4 | 6e-06 | 23/46 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +4.9 | 7e-05 | 23/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.002 | 22/47 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.003 | 22/48 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +4.0 | 0.003 | 22/47 (HT-29, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 19/48 (NCI-H460, HOP62, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.005 | 21/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.005 | 20/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.005 | 21/47 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.006 | 20/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.009 | 18/47 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.009 | 17/47 (SNU-1, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9056.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A498 0.106×, NCI-H2030 0.0587×, NCI-H2347 0.158×, NCI-H1792 0.106×, …; ⚠ toxic; transcription drop); [[Selinexor (drug)]] 5 µM in 2 lines (CFPAC-1 0.128×, NCI-H2347 0.253×; ⚠ cell-cycle shift, explains ~12% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.166×, RKO 0.252×; ⚠ cell-cycle shift, explains ~0% of this change); [[Allantoin (drug)]] 0.5 µM in 1 line (CHP-212 0.0934×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.580×** | -7.0 | 2e-09 | 27/44 (hTERT-HPNE, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -6.7 | 6e-09 | 21/35 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tofacitinib (drug)]] 5 µM |  | **0.804×** | -4.5 | 0.001 | 22/47 (CFPAC-1, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.740×** | -3.9 | 0.015 | 17/47 (A-172, C32, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.800× | -3.1 | 0.20 | 17/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.1 | 0.20 | 3/48 (SW 1271, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.2 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.25× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 1 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 10.2× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 35.8 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 15.5× (z +12.7) | [[Selinexor (drug)]] 5 µM 0.253× (z -17.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[SW480 (line)]] | alt | 20.0 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 13.9× (z +12.4) | — |
| [[SNU-423 (line)]] | alt | 116 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -13.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A498 (line)]] | wt | 89.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -20.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.4) | [[Selinexor (drug)]] 5 µM 0.128× (z -22.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[NCI-H1573 (line)]] | alt | 29.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 22.7× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 63.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.3× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 31.2 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.5× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -19.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 48.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 56.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 77.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.96× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 19.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 15.3× (z +9.1) | — |
| [[C32 (line)]] | wt | 24.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 78.4× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 90.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.3× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.160× (z -11.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 50.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 17.9× (z +10.7) | — |
| [[RKO (line)]] | wt | 27.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.9× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 41.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.9× (z +11.3) | — |
| [[BT-474 (line)]] | alt | 21.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 30.2× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 42.5 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0934× (z -9.4) |
| [[COLO 205 (line)]] | alt | 33.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 28.3× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 43.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.9× (z +10.6) | — |
| [[HT-29 (line)]] | alt | 22.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.1× (z +9.7) | — |
| [[KATO III (line)]] | alt | 28.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.9× (z +9.1) | — |
| [[LoVo (line)]] | wt | 20.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 36.4× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.4× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 31.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.7× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 23.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.35× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 18.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 26.5× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 30.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.8× (z +9.6) | — |
| [[A-172 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAMPT]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 475 |
| [[AVPI1]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[BCL6]] | +0.62 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 477 |
| [[PTGES]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[FTH1]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[DEPP1]] | +0.57 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[C1R]] | +0.56 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[HIF1A]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[DDIT4]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA; STRING 415 |
| [[TSC22D3]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[SOD2]] | +0.55 | +0.53 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PLIN2]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIPAL1]] | -0.53 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[DCTD]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SH3D19]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[B4GALT6]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CCND1]] | -0.49 | -0.46 / -0.42 | both halves | 4e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SH3TC2]] | -0.47 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[SH3TC2-DT]] | -0.47 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TRBC2]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[LTBP2]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MIR4280HG]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PRDM5]] | -0.46 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[ELK4]] | -0.45 | -0.49 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA12]] | B | CA12 activity raises NFIL3's level | lines that do not express CA12 (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without CA12 | 0.006 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[RHCG]] | B | RHCG activity raises NFIL3's level | lines that do not express RHCG (33) vs lines expressing it (17) | 1.85× lower at baseline in the lines without RHCG | 0.008 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[MLLT3]] | B | MLLT3 activity raises NFIL3's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without MLLT3 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[LOX]] | B | LOX activity raises NFIL3's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.06× lower at baseline in the lines without LOX | 0.023 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[PLIN2]] | B | PLIN2 activity raises NFIL3's level | lines that do not express PLIN2 (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without PLIN2 | 0.024 | ⚠ within organs, on part of the lines; also absent: AXL, UBE2Q2P13, SLC2A3 |
| [[CD38]] | B | CD38 activity raises NFIL3's level | lines that do not express CD38 (35) vs lines expressing it (15) | 1.52× lower at baseline in the lines without CD38 | 0.034 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent |
| [[MIR4280HG]] | B | MIR4280HG activity raises NFIL3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.50× lower at baseline in the lines without MIR4280HG | 0.061 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[FAM13A]] | B | FAM13A activity raises NFIL3's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FAM13A | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[PTGES]] | B | PTGES activity raises NFIL3's level | lines that do not express PTGES (17) vs lines expressing it (33) | 1.69× lower at baseline in the lines without PTGES | 0.066 | ⚠ within organs, on part of the lines; also absent: C1R, GPX3, CFAP300 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 17.4); signed map (17.6, 26.6). **Vector** length 128, 37.7% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-4 and Interleukin-13 signaling* (reactome, mean cos +0.52 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +20.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +5.9 |
|  | [[Trametinib (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.8 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.7 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.6 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.3 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.4 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.8 | -0.1 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor, interleukin 3 regulated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:91,409,045-91,423,832 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E4BP4, NFIL3A, NF-IL3A; previously IL3BP1 |
| Gene groups (HGNC) | Basic leucine zipper proteins |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, IL2_STAT5_SIGNALING, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16649](https://www.uniprot.org/uniprotkb/Q16649) (Nuclear factor interleukin-3-regulated protein):

> Acts as a transcriptional regulator that recognizes and binds to the sequence 5'-[GA]TTA[CT]GTAA[CT]-3', a sequence present in many cellular and viral promoters. Represses transcription from promoters with activating transcription factor (ATF) sites. Represses promoter activity in osteoblasts (By similarity). Represses transcriptional activity of PER1 (By similarity). Represses transcriptional activity of PER2 via the B-site on the promoter (By similarity). Activates transcription from the …

**Summary**, from NCBI Gene [4783](https://www.ncbi.nlm.nih.gov/gene/4783):

> The protein encoded by this gene is a transcriptional regulator that binds as a homodimer to activating transcription factor (ATF) sites in many cellular and viral promoters. The encoded protein represses PER1 and PER2 expression and therefore plays a role in the regulation of circadian rhythm. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:7787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7787) · Entrez [4783](https://www.ncbi.nlm.nih.gov/gene/4783) · UniProt [Q16649](https://www.uniprot.org/uniprotkb/Q16649) · Ensembl [ENSG00000165030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165030)

## Data

Gene col 9056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9056); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9056]; `tensor/DDL_lfc|DDL_z.npy` [9056]; `embed/gene_vectors.npy` [9056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9056 or target_col == 9056). Every well: [[NFIL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/NFIL3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

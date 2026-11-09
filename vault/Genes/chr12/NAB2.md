---
symbol: "NAB2"
type: "gene"
col: 9377
ensembl_id: "ENSG00000166886"
name: "NGFI-A binding protein 2"
location: "12q13.3"
module: 162
arm: "+"
pooled_cpm: 17.4
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 10
tags: ["gene", "module/162", "written"]
generated_by: "tahoemap"
---

# NAB2

*NGFI-A binding protein 2* — 12q13.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> NAB2 encodes a transcriptional corepressor with no DNA-binding domain of its own, acting through EGR-family factors to shut down their output.

## What it is

NAB2 — NGFI-A-binding protein 2, also known as EGR1-binding protein 2 or MADER — was isolated as a repressor of NGFI-A (EGR1) and Krox20 (EGR2). Its first conserved domain binds the R1 region of NGFI-A, and repression is carried out at least partly by recruiting the CHD4 subunit of the NuRD remodelling and deacetylase complex. The circuit is a feedback loop: EGR factors bind sites in the NAB2 promoter and induce it, so NAB2 accumulates after the immediate-early burst and terminates it. The gene sits at 12q13.3, where a recurrent NAB2-STAT6 fusion defines solitary fibrous tumour.

## What is uncertain

Its regulon in this collection holds only a handful of targets, which puts the score close to a single-gene measurement; and because NAB2 represses, whether coherent movement in those targets means high or low activity depends on sign conventions the collections apply inconsistently to repressors. Immediate-early signalling is also moved by the stress and translation-inhibiting compounds that drive [[Readthrough spillover]]. One practical trap: the yeast protein Nab2 is an unrelated poly(A)-RNA-binding protein, and much of what a literature search returns under this name concerns that.

## References

- Svaren et al., 1996, Molecular and Cellular Biology — identified NAB2 as a corepressor of NGFI-A and Krox20 induced by proliferative and differentiative stimuli.
- Robinson et al., 2013, Nature Genetics — identified recurrent NAB2-STAT6 fusions in solitary fibrous tumour.
- Chmielecki et al., 2013, Nature Genetics — independently found the recurrent NAB2-STAT6 fusion in solitary fibrous tumours.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.04× (z +7.7, q 7e-12, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.587× (z -10.0, q 1e-20, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TGFB1]] (+0.61, fdr 1e-05), [[SERTAD3]] (+0.58, fdr 1e-05), [[SPATA2L]] (+0.57, fdr 4e-05); moves opposite to [[VRK2]] (-0.56, fdr 3e-05), [[CLCC1]] (-0.51, fdr 4e-05), [[TLCD4-RWDD3]] (-0.49, fdr 1e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[NCKAP5L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.04×** | +7.7 | 7e-12 | 30/45 (A-427, NCI-H1573, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.2 | 2e-07 | 25/44 (HEC-1-A, A-427, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.8 | 4e-04 | 20/43 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +4.0 | 0.011 | 18/42 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.22 | 17/43 (HT-29, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -10.0 | 1e-20 | 31/44 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -8.3 | 4e-14 | 34/43 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.540×** | -8.1 | 7e-14 | 31/44 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -6.9 | 6e-10 | 25/45 (hTERT-HPNE, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -6.3 | 3e-08 | 29/45 (SK-MEL-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -6.0 | 2e-07 | 20/32 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -5.1 | 2e-05 | 24/44 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -4.6 | 3e-04 | 20/40 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.708×** | -4.6 | 3e-04 | 20/45 (NCI-H23, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 5e-04 | 18/45 (CHP-212, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 5e-04 | 18/44 (HepG2/C3A, A549, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.784×** | -4.4 | 5e-04 | 19/45 (HCT15, SW 1088, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.733×** | -4.3 | 8e-04 | 19/45 (HCT15, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.798×** | -4.1 | 0.001 | 18/45 (HCT15, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -4.1 | 0.002 | 21/44 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.002 | 20/45 (CHP-212, NCI-H23, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.778×** | -4.0 | 0.002 | 16/45 (HCT15, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 45.4 | 2 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.24× (z +9.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -15.5) |
| [[hTERT-HPNE (line)]] | wt | 29.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.204× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -11.1) |
| [[NCI-H460 (line)]] | wt | 15.0 | 4 (4 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.70× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.133× (z -13.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.0) |
| [[HOP62 (line)]] | alt | 20.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 39.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0760× (z -17.1) ⚠ toxic · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 37.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -9.4) |
| [[A498 (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.0) |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0555× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.143× (z -11.9) |
| [[SW480 (line)]] | alt | 13.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -9.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0483× (z -16.3) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.8) |
| [[H4 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 38.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 11.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.73× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -11.8) |
| [[RKO (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -8.9) |
| [[SW48 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFB1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SERTAD3]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SPATA2L]] | +0.57 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[ELK1]] | +0.56 | +0.64 / +0.47 | both halves | 2e-05 | pathway: NGF-stimulated transcription |
| [[DUSP2]] | +0.54 | +0.41 / +0.44 | both halves | 4e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE |
| [[PPP1R18]] | +0.54 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[PLA2G15]] | +0.54 | +0.55 / +0.36 | both halves | 9e-05 |  |
| [[ING1]] | +0.54 | +0.48 / +0.39 | both halves | 5e-05 |  |
| [[NCKAP5L]] | +0.53 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[STMN3]] | +0.52 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[PHF13]] | +0.51 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MEF2D]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 | pathway: NGF-stimulated transcription |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VRK2]] | -0.56 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[CLCC1]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[TLCD4-RWDD3]] | -0.49 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[KIF21A]] | -0.48 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[IDE]] | -0.46 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[HGD]] | -0.46 | -0.58 / -0.21 | both halves | 6e-04 |  |
| [[VBP1]] | -0.45 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[NSMAF]] | -0.44 | -0.36 / -0.29 | both halves | 2e-04 |  |
| [[VPS36]] | -0.44 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[DERA]] | -0.44 | -0.51 / -0.23 | both halves | 6e-04 |  |
| [[RCC1L]] | -0.44 | -0.44 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[QRSL1]] | -0.44 | -0.49 / -0.24 | both halves | 4e-04 |  |
| [[PSMA3]] | -0.43 | -0.42 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NAB2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCKAP5L]] | C | NAB2 activity raises NCKAP5L's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without NAB2 | 0.007 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| cells under [[Lonafarnib (drug)]] 5 µM | C | [[FSD1L]], NAB2 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express FSD1L, NAB2 (3) vs lines expressing them (45) | the lines without FSD1L, NAB2: 0.09× the cells of the other lines | 0.013 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent genes |
| [[MAD2L2]] | C | NAB2 activity raises MAD2L2's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without NAB2 | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[LINC00659]] | C | NAB2 activity lowers LINC00659's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 5.09× higher at baseline in the lines without NAB2 | 0.029 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[GALE]] | C | NAB2 activity weakens GALE's drug response | lines that do not express NAB2 (3) vs lines expressing it (44) | the lines without NAB2 respond 1.76× as strongly (z diff -1.49); strongest at Digitoxin 5 µM: 0.29x vs 0.64x (z diff -4.4) | 0.030 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[HGD]] | C | NAB2 activity lowers HGD's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 5.29× higher at baseline in the lines without NAB2 | 0.036 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[SH3GL1]] | C | NAB2 activity raises SH3GL1's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without NAB2 | 0.047 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| cells under [[MK-3903 (drug)]] 5 µM | C | [[FSD1L]], NAB2 activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express FSD1L, NAB2 (3) vs lines expressing them (45) | the lines without FSD1L, NAB2: 0.69× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent genes |
| [[TGFB1]] | C | NAB2 activity raises TGFB1's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 4.11× lower at baseline in the lines without NAB2 | 0.081 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | C | [[FSD1L]], NAB2 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express FSD1L, NAB2 (3) vs lines expressing them (45) | the lines without FSD1L, NAB2: 1.27× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, -28.5); signed map (-28.2, 30.5). **Vector** length 99.8, 22.5% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.1 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | -4.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.0 | +1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.5 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.1 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | NGFI-A binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,089,043-57,095,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MADER |
| Gene groups (HGNC) | NGFI-A binding protein family |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 7 pathways, smallest: EGR2 and SOX10-mediated initiation of Schwann cell myelination; NGF-stimulated transcription; Nuclear Events (kinase and transcription factor activation) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15742](https://www.uniprot.org/uniprotkb/Q15742) (NGFI-A-binding protein 2):

> Acts as a transcriptional repressor for zinc finger transcription factors EGR1 and EGR2. Isoform 2 lacks repression ability (By similarity).

**Summary**, from NCBI Gene [4665](https://www.ncbi.nlm.nih.gov/gene/4665):

> This gene encodes a member of the family of NGFI-A binding (NAB) proteins, which function in the nucleus to repress transcription induced by some members of the EGR (early growth response) family of transactivators. NAB proteins can homo- or hetero-multimerize with other EGR or NAB proteins through a conserved N-terminal domain, and repress transcription through two partially redundant C-terminal domains. Transcriptional repression by the encoded protein is mediated in part by interactions with …

**Accessions** — [HGNC:7627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7627) · Entrez [4665](https://www.ncbi.nlm.nih.gov/gene/4665) · UniProt [Q15742](https://www.uniprot.org/uniprotkb/Q15742) · Ensembl [ENSG00000166886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166886)

## Data

Gene col 9377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9377); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9377]; `tensor/DDL_lfc|DDL_z.npy` [9377]; `embed/gene_vectors.npy` [9377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9377 or target_col == 9377). Every well: [[NAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/NAB2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

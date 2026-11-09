---
symbol: "BBC3"
type: "gene"
col: 2583
ensembl_id: "ENSG00000105327"
name: "BCL2 binding component 3"
location: "19q13.32"
module: 59
arm: "+"
pooled_cpm: 22.99
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/059", "written"]
generated_by: "tahoemap"
---

# BBC3

*BCL2 binding component 3* — 19q13.32

> [!summary] In one line
> BBC3 encodes PUMA, the BH3-only protein that is p53's most direct and most quantitatively important route to apoptosis.

## What it is

BBC3 (BCL-2 binding component 3) encodes PUMA, a small BH3-only member of the BCL-2 family. It is close to undetectable in unstressed cells and is induced strongly and rapidly by p53 through p53 response elements in its promoter. The protein localises to mitochondria and binds every anti-apoptotic BCL-2 family member with high affinity, which frees sequestered activators such as BIM and BID and leaves BAX and BAK unrestrained — so PUMA does not form pores itself, it removes the restraint on the proteins that do. Within the p53 response it is the component whose loss subtracts the most apoptosis: in mouse genetics, Puma deficiency accounts for the bulk of p53-dependent death after DNA damage in lymphoid cells, and combined loss of Puma and Noxa reproduces much of what p53 loss does in that setting.

PUMA is not only a p53 gene. Transcription is also driven by FOXO3A, by E2F1, by glucocorticoid receptor signalling and by growth-factor or cytokine withdrawal, giving it a substantial p53-independent induction repertoire. Clinically, basal and inducible PUMA levels contribute to chemotherapy and glucocorticoid sensitivity and to how cells respond to BH3-mimetic drugs, though PUMA itself is not a drug target.

## What is uncertain

Two things qualify PUMA as a readout here. First, its non-p53 inducers are real and several of them — growth-factor withdrawal, glucocorticoid signalling, FOXO3A activation — are exactly what a 24 h drug exposure can produce, so induction in a pooled, mixed-genotype panel is not by itself proof of p53 activity. That matters wherever the logic of [[p53 nullification in cancer cell lines]] is used to sign a gene by genotype. Second, apoptosis is self-censoring in single-cell data: dying cells lose mRNA and are preferentially lost at dissociation and quality filtering, so the cells carrying the strongest PUMA signal are the ones least likely to be counted. The bias runs toward understating the apoptotic arm and is hard to correct.

Mechanistically, whether PUMA is a direct activator of BAX or only a derepressor of anti-apoptotic proteins is still unresolved, with PUMA sitting awkwardly between the two models. And its necessity is lineage-dependent: the strong genetic evidence comes largely from lymphoid cells, while epithelial lines often tolerate PUMA loss with less effect on p53-driven death.

## References

- Nakano and Vousden, 2001, Molecular Cell — identified PUMA as a BH3-only gene induced by p53.
- Yu et al., 2001, Molecular Cell — identified PUMA as a p53-induced gene that triggers rapid apoptosis in colorectal cancer cells.
- Villunger et al., 2003, Science — showed Puma and Noxa mediate much of p53-dependent and drug-induced apoptosis in mouse cells.
- Jeffers et al., 2003, Cancer Cell — showed Puma is an essential mediator of both p53-dependent and p53-independent apoptotic pathways.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.57× (z +11.8, q 2e-29, up in 39 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.47× (z +11.0, q 1e-25, up in 35 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.372× (z -8.7, q 1e-15, down in 40 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.584× (z -4.7, q 6e-04, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIM3]] (+0.74, fdr 7e-06), [[JUND]] (+0.64, fdr 7e-06), [[RILP]] (+0.63, fdr 1e-05); moves opposite to [[AHSA1]] (-0.59, fdr 1e-05), [[NUP205]] (-0.58, fdr 1e-05), [[LAMB1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BTG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.57×** | +11.8 | 2e-29 | 39/45 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.47×** | +11.0 | 1e-25 | 35/45 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.84×** | +7.3 | 6e-11 | 35/46 (A549, LOX-IMVI, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +6.7 | 4e-09 | 33/42 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.89×** | +5.4 | 7e-06 | 31/45 (PANC-1, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +4.7 | 2e-04 | 27/45 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 0.002 | 22/45 (HS-578T, A549, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.85×** | +3.9 | 0.007 | 27/44 (LOX-IMVI, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.011 | 21/46 (HT-29, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.6 | 0.015 | 19/44 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.015 | 22/45 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.14×** | +3.5 | 0.020 | 20/44 (SW48, BT-474, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.074 | 18/47 (KATO III, SW48, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.074 | 16/47 (HT-29, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2583.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.372×** | -8.7 | 1e-15 | 40/46 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.584×** | -4.7 | 6e-04 | 25/46 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.580×** | -4.6 | 7e-04 | 23/44 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.719×** | -4.1 | 0.006 | 22/47 (SW1417, HT-29, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -3.8 | 0.019 | 21/32 (MIA PaCa-2, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.446×** | -3.7 | 0.019 | 21/45 (SW48, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.458×** | -3.6 | 0.025 | 22/45 (SW1417, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.773×** | -3.2 | 0.095 | 19/47 (CFPAC-1, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.701× | -3.0 | 0.16 | 19/45 (HT-29, MIA PaCa-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 53.1 | 1 | 5 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.24× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -15.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.83× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -14.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 65.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.62× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +20.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.93× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.18× (z +11.2) | — |
| [[SW48 (line)]] | wt | 54.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.09× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 22.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.94× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.137× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 56.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.13× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.34× (z +8.6) | — |
| [[J82 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +13.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 46.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Auranofin (drug)]] 5 µM 0.272× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.59× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.37× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 15.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -16.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.7× (z +21.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 13.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 10.3× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 8.24 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.66× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.91× (z +9.0) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[JUND]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[RILP]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.61 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[RPS27L]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[NFKBIA]] | +0.60 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[CBX4]] | +0.60 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[GLIS2]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[DUSP8]] | +0.59 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.59 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[ACHE]] | +0.58 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ELF3]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.59 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[NUP205]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[LAMB1]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PTDSS1]] | -0.56 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[PAICS]] | -0.55 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.55 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SUV39H2]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[NAA50]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.54 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[CCT3]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TMX3]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTG2]] | B | BTG2 activity raises BBC3's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without BTG2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens BBC3's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 0.77× as strongly (z diff +0.87); strongest at Homoharringtonine 0.5 µM: 2.34x vs 4.06x (z diff +2.8) | 0.467 over the table, 0.023 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.680). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (23.1, -1.4); signed map (46.9, -1.5). **Vector** length 138, 43.3% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.1 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.0 | +6.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.5 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 binding component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:47,220,822-47,232,766 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JFY1, PUMA |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only; MicroRNA protein coding host genes |
| Reactome | 11 pathways, smallest: Activation of PUMA and translocation to mitochondria; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members; FOXO-mediated transcription of cell death genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PG8](https://www.uniprot.org/uniprotkb/Q96PG8) (Bcl-2-binding component 3, isoforms 3/4):

> [Isoform 3]: Does not affect cell growth.

**Summary**, from NCBI Gene [27113](https://www.ncbi.nlm.nih.gov/gene/27113):

> This gene encodes a member of the BCL-2 family of proteins. This family member belongs to the BH3-only pro-apoptotic subclass. The protein cooperates with direct activator proteins to induce mitochondrial outer membrane permeabilization and apoptosis. It can bind to anti-apoptotic Bcl-2 family members to induce mitochondrial dysfunction and caspase activation. Because of its pro-apoptotic role, this gene is a potential drug target for cancer therapy and for tissue injury. Alternative splicing …

**Accessions** — [HGNC:17868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17868) · Entrez [27113](https://www.ncbi.nlm.nih.gov/gene/27113) · UniProt [Q96PG8](https://www.uniprot.org/uniprotkb/Q96PG8) · Ensembl [ENSG00000105327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105327)

## Data

Gene col 2583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2583); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2583]; `tensor/DDL_lfc|DDL_z.npy` [2583]; `embed/gene_vectors.npy` [2583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2583 or target_col == 2583). Every well: [[BBC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/BBC3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

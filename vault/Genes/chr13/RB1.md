---
symbol: "RB1"
type: "gene"
col: 6335
ensembl_id: "ENSG00000139687"
name: "RB transcriptional corepressor 1"
location: "13q14.2"
module: 146
arm: "-"
pooled_cpm: 153.25
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/146", "written"]
generated_by: "tahoemap"
---

# RB1

*RB transcriptional corepressor 1* — 13q14.2

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> RB1 encodes the retinoblastoma protein, the pocket protein that holds E2F transcription factors inactive until CDK phosphorylation releases them and licenses S-phase entry.

## What it is

The first tumour suppressor cloned. Its pocket domain binds the E2F transactivation domain while a separate LxCxE surface recruits histone deacetylases and chromatin modifiers, so RB does not merely block E2F but actively represses its target promoters. RB is hypophosphorylated in G0 and early G1, then progressively phosphorylated by cyclin D–CDK4/6 and cyclin E–CDK2, releasing E2F. The [[CDKN2A]]–CDK4–RB–E2F axis is disabled in most cancers, by RB1 loss in retinoblastoma and small-cell lung cancer or by p16 deletion and cyclin D amplification — and intact RB is what CDK4/6 inhibitors require. p53 reaches RB indirectly, through [[CDKN1A]]: p21 inhibits the CDKs, RB stays hypophosphorylated, E2F targets stay off.

## What is uncertain

Whether this is about RB1 at all. Its regulon overlaps the E2F and DREAM target set that dominates any arrest response, so an association of this shape would appear wherever some conditions slow the cycle, and it cannot be separated from p21 induction ([[The p21-DREAM axis]]). RB function is set by phosphorylation, not transcript level, so target-based inference and RB1 mRNA answer different questions.

## References

- Friend et al., 1986, Nature — identified the retinoblastoma susceptibility gene.
- Buchkovich, Duffy & Harlow, 1989, Cell — showed that the RB protein is phosphorylated in a cell-cycle-dependent manner.
- Litovchick et al., 2007, Molecular Cell — characterised the p130–E2F4 DREAM complex repressing cell-cycle-dependent genes in quiescence.
- Dyson, 2016, Genes & Development — review reassessing RB1 as prototype tumour suppressor and the gaps in the E2F-only account.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.52× (z +12.8, q 6e-35, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.726× (z -9.8, q 1e-19, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAP29]] (+0.56, fdr 1e-05), [[AP1S2]] (+0.53, fdr 3e-05), [[SCYL2]] (+0.53, fdr 1e-05); moves opposite to [[EIF3E]] (-0.57, fdr 1e-05), [[POP1]] (-0.55, fdr 1e-05), [[ARHGEF10L]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); 5 go from it, the strongest it → [[ENSG00000234147]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +12.8 | 6e-35 | 36/48 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.31×** | +8.3 | 2e-14 | 28/48 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.20×** | +7.9 | 5e-13 | 22/48 (SW480, NCI-H2347, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +7.4 | 2e-11 | 29/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.28×** | +7.1 | 1e-10 | 29/48 (COLO 205, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.23×** | +6.4 | 1e-08 | 29/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +6.4 | 1e-08 | 27/50 (LS 180, SW48, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.64×** | +6.0 | 1e-07 | 34/48 (HOP62, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +6.0 | 2e-07 | 26/48 (LS 180, SW48, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +5.9 | 2e-07 | 29/49 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | 1.15× | +4.0 | 0.004 | 22/45 (A498, C-33 A, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.13× | +3.8 | 0.006 | 19/48 (LoVo, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.12× | +3.4 | 0.029 | 12/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | 1.12× | +3.4 | 0.031 | 18/44 (LS 180, MIA PaCa-2, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.12× | +3.1 | 0.083 | 20/48 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Naproxen (drug)]] 5 µM |  | 1.11× | +3.0 | 0.091 | 5/48 (CFPAC-1, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.726×** | -9.8 | 1e-19 | 34/48 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.778×** | -7.2 | 2e-10 | 30/48 (A-172, HT-29, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.791×** | -7.1 | 2e-10 | 28/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.799×** | -6.8 | 1e-09 | 27/48 (HOP62, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.814×** | -6.3 | 4e-08 | 25/48 (NCI-H661, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.876× | -5.7 | 1e-06 | 18/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.884× | -5.3 | 9e-06 | 11/48 (AsPC-1, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.866× | -4.4 | 9e-04 | 20/49 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.831×** | -4.0 | 0.004 | 16/48 (KATO III, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.876× | -4.0 | 0.004 | 10/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.836× | -3.9 | 0.005 | 19/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.727×** | -3.9 | 0.005 | 21/48 (AsPC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.727×** | -3.9 | 0.005 | 19/45 (A-172, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.877× | -3.8 | 0.005 | 14/48 (PANC-1, A549, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.882× | -3.8 | 0.005 | 16/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.883× | -3.8 | 0.005 | 14/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.009 | 15/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.885× | -3.6 | 0.011 | 9/48 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.896× | -3.2 | 0.037 | 10/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.866× | -3.1 | 0.047 | 11/48 (LOX-IMVI, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.779×** | -3.0 | 0.059 | 14/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 243 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.79× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 189 | 3 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +15.5) | [[Ixazomib citrate (drug)]] 5 µM 0.591× (z -8.5) |
| [[LoVo (line)]] | wt | 99.3 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 140 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.13× (z +12.8) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +10.4) | — |
| [[SW480 (line)]] | alt | 162 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +14.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 129 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +14.1) | — |
| [[RKO (line)]] | wt | 163 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 79.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.7) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SHP-77 (line)]] | alt | 106 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 156 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.2) | — |
| [[A-172 (line)]] | wt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.649× (z -10.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.81× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 184 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 73.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.97× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 244 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 113 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.9) | — |
| [[HT-29 (line)]] | alt | 151 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.533× (z -8.7) |
| [[J82 (line)]] | alt | 258 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.610× (z -9.1) |
| [[KATO III (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.546× (z -8.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 208 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 77.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -9.9) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -9.3) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.550× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 131 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.415× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 137 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 224 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 147 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 259 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 119 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP29]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[AP1S2]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[SCYL2]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PFN1]] | +0.51 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[RO60]] | +0.50 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[AXL]] | +0.50 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[NEMP1]] | +0.49 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ARPC2]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[SLC30A9]] | +0.48 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[TMEM107]] | +0.48 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[NPAT]] | +0.48 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[ACTR2]] | +0.47 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF3E]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[POP1]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ARHGEF10L]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ZSCAN2]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SFXN4]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[TRIM16]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[HDHD3]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[JKAMP]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[HSPA1B]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[COASY]] | -0.48 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[LINC01012]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PISD]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises RB1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENSG00000234147]] | C | the direction of RB1's effect on ENSG00000234147's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of RB1 in 3 lines vs 25 not recorded | the RB1-altered lines respond the other way (z diff +8.19); strongest at Homoharringtonine 5 µM: 3.88x vs 0.33x (z diff +17.6) | 0.013 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[BAZ2B]] | C | the direction of RB1's effect on BAZ2B's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of RB1 in 3 lines vs 45 not recorded | the RB1-altered lines respond 0.52× as strongly (z diff +3.33); strongest at Panobinostat 0.05 µM: 1.04x vs 0.59x (z diff +6.5) | 0.040 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded; target measured in part of the lines; artifact flags |
| [[HELLS]] | C | RB1 activity strengthens HELLS's drug response | recorded loss-of-function mutation of RB1 in 3 lines vs 46 not recorded | the RB1-altered lines respond 0.48× as strongly (z diff +1.67); strongest at Dinaciclib 0.05 µM: 0.94x vs 3.43x (z diff +9.1) | 0.131 over the table, 0.004 within its group | ⚠ within its group only (a lead); few lines (3 vs 46); tissue-confounded; across organs; artifact flags |
| [[NPPB]] | C | RB1 activity lowers NPPB's level | recorded loss-of-function mutation of RB1 in 3 lines vs 46 not recorded | 6.83× higher at baseline in the RB1-altered lines | 0.328 over the table, 0.067 within its group | ⚠ within its group only (a lead); few lines (3 vs 46); tissue-confounded; across organs |
| [[SLIT2]] | C | RB1 activity strengthens SLIT2's drug response | recorded loss-of-function mutation of RB1 in 3 lines vs 26 not recorded | the RB1-altered lines respond 0.09× as strongly (z diff +4.05); strongest at Idarubicin (hydrochloride) 5 µM: 0.77x vs 4.76x (z diff +10.8) | 0.610 over the table, 0.035 within its group | ⚠ within its group only (a lead); few lines (3 vs 46); tissue-confounded; across organs; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-57.3, 3.1); signed map (-5.2, 38.2). **Vector** length 126, 36.3% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.4 | +12.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +4.2 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +4.1 | +6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.9 | +7.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.9 | +1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.8 | +0.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -8.9 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.9 | -9.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.1 | -5.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.9 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.7 | -6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.7 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RB transcriptional corepressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:48,303,744-48,599,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RB, PPP1R130; previously OSRC |
| Gene groups (HGNC) | Receptor ligands |
| Hallmark sets | MYOGENESIS, P53_PATHWAY |
| Reactome | 59 pathways, smallest: Phosphorylation of proteins involved in G1/S transition by active Cyclin E:Cdk2 complexes; Replication of the SARS-CoV-1 genome; Replication of the SARS-CoV-2 genome |
| Matched by | ensembl_id |

**Function**, from UniProt [P06400](https://www.uniprot.org/uniprotkb/P06400) (Retinoblastoma-associated protein):

> Tumor suppressor that is a key regulator of the G1/S transition of the cell cycle. The hypophosphorylated form binds transcription regulators of the E2F family, preventing transcription of E2F-responsive genes. Both physically blocks E2Fs transactivating domain and recruits chromatin-modifying enzymes that actively repress transcription. Cyclin and CDK-dependent phosphorylation of RB1 induces its dissociation from E2Fs, thereby activating transcription of E2F responsive genes and triggering …

**Summary**, from NCBI Gene [5925](https://www.ncbi.nlm.nih.gov/gene/5925):

> The protein encoded by this gene is a negative regulator of the cell cycle and was the first tumor suppressor gene found. The encoded protein also stabilizes constitutive heterochromatin to maintain the overall chromatin structure. The active, hypophosphorylated form of the protein binds transcription factor E2F1. Defects in this gene are a cause of childhood cancer retinoblastoma (RB), bladder cancer, and osteogenic sarcoma. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9884) · Entrez [5925](https://www.ncbi.nlm.nih.gov/gene/5925) · UniProt [P06400](https://www.uniprot.org/uniprotkb/P06400) · Ensembl [ENSG00000139687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139687)

## Data

Gene col 6335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6335); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6335]; `tensor/DDL_lfc|DDL_z.npy` [6335]; `embed/gene_vectors.npy` [6335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6335 or target_col == 6335). Every well: [[RB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/RB1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

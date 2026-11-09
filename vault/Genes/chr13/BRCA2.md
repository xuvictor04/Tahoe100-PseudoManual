---
symbol: "BRCA2"
type: "gene"
col: 6320
ensembl_id: "ENSG00000139618"
name: "BRCA2 DNA repair associated"
location: "13q13.1"
module: 91
arm: "+"
pooled_cpm: 58.5
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/091", "written"]
generated_by: "tahoemap"
---

# BRCA2

*BRCA2 DNA repair associated* — 13q13.1

> [!summary] In one line
> BRCA2 is the mediator that loads RAD51 onto resected DNA ends for homologous recombination, and one of the two classical hereditary breast and ovarian cancer genes.

## What it is

BRCA2 is a very large protein whose BRC repeats and DNA-binding domain deliver RAD51 to single-stranded DNA and displace RPA, the nucleation step of homologous recombination. The same activity stabilises RAD51 on stalled forks, a function separable from repair of frank breaks. Monoallelic germline loss confers raised risk of breast, ovarian, pancreatic and prostate cancer; biallelic hypomorphic loss causes the FANCD1 subtype of Fanconi anaemia. Loss of BRCA2 is the canonical setting for PARP-inhibitor synthetic lethality and platinum sensitivity; restored recombination is a recognised resistance route.

## What is uncertain

Whether p53 represses BRCA2 at all in the direct sense is doubtful; the better-supported view is that p53 is an activator whose apparent repression of cell-cycle genes is relayed through p21. The direction label below is also a selection outcome, so it describes the gene rather than demonstrating specificity. And transcript level is a weak proxy for recombination proficiency: a modest fall in BRCA2 mRNA at 24 h is not evidence of induced "BRCAness".

## References

- Wooster et al., 1995, Nature — identification of the BRCA2 gene.
- Moynahan et al., 2001, Molecular Cell — BRCA2 is required for homology-directed repair of double-strand breaks.
- Howlett et al., 2002, Science — biallelic BRCA2 mutations cause Fanconi anaemia, defining FANCD1.
- Jensen et al., 2010, Nature — purified human BRCA2 promotes RAD51-mediated recombination.
- Farmer et al., 2005, Nature — PARP inhibition is selectively lethal in BRCA-deficient cells.
- Engeland, 2018, Cell Death and Differentiation — review of indirect transcriptional repression through the p53-p21-DREAM route.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.81× (z +8.6, q 5e-15, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.500× (z -9.9, q 2e-20, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MASTL]] (+0.85, fdr 7e-06), [[ZNF724]] (+0.84, fdr 7e-06), [[ESCO2]] (+0.84, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRRN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +8.6 | 5e-15 | 37/48 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +7.4 | 3e-11 | 30/48 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.48×** | +5.3 | 2e-05 | 29/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +5.2 | 2e-05 | 28/48 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.24×** | +4.5 | 7e-04 | 23/48 (HT-29, SW480, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +4.5 | 8e-04 | 19/48 (HT-29, A549, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +4.3 | 0.001 | 23/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +4.2 | 0.002 | 23/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.31×** | +3.9 | 0.005 | 18/48 (HT-29, SW480, …) | all doses, flat |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.005 | 16/48 (COLO 205, SW 900, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.32×** | +3.8 | 0.006 | 24/48 (HT-29, NCI-H460, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +3.6 | 0.013 | 15/48 (HT-29, LS 180, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.015 | 20/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.020 | 20/48 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.3 | 0.039 | 10/48 (HCT15, NCI-H23, …) | top dose only |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.052 | 14/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.052 | 14/48 (HT-29, LS 180, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.053 | 11/48 (MIA PaCa-2, LS 180, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.060 | 15/48 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.060 | 22/48 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.060 | 16/48 (J82, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.060 | 14/48 (PANC-1, HOP62, …) | two highest doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.060 | 11/48 (KATO III, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.500×** | -9.9 | 2e-20 | 37/48 (KATO III, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -9.4 | 2e-18 | 38/47 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.650×** | -9.2 | 5e-18 | 33/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.643×** | -6.7 | 3e-09 | 29/48 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -6.4 | 2e-08 | 33/48 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.659×** | -6.3 | 3e-08 | 30/48 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -6.1 | 9e-08 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -6.1 | 9e-08 | 31/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.488×** | -5.7 | 8e-07 | 28/43 (SNU-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.699×** | -5.4 | 3e-06 | 28/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.627×** | -5.0 | 2e-05 | 28/48 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.535×** | -5.0 | 3e-05 | 26/48 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 1e-04 | 26/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -4.5 | 2e-04 | 23/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.659×** | -4.5 | 2e-04 | 28/48 (MIA PaCa-2, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 8e-04 | 23/48 (J82, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -4.2 | 9e-04 | 23/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.017 | 17/48 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.019 | 19/48 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.857× | -3.3 | 0.024 | 18/48 (COLO 205, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 50.5 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -14.0) |
| [[J82 (line)]] | alt | 153 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -10.9) ⚠ toxic · without an alert: [[Belinostat (drug)]] 0.5 µM 0.437× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 29.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +20.7) | — |
| [[KATO III (line)]] | alt | 86.1 | 0 | 4 | — | [[Bortezomib (drug)]] 0.05 µM 0.242× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 87.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.318× (z -11.0) |
| [[C32 (line)]] | wt | 44.8 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.7) | [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -8.8) |
| [[COLO 205 (line)]] | alt | 146 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 145 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.287× (z -12.9) |
| [[LS 180 (line)]] | wt | 29.0 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.266× (z -11.7) |
| [[SW480 (line)]] | alt | 72.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -10.8) |
| [[A-172 (line)]] | wt | 71.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.301× (z -12.5) |
| [[A498 (line)]] | wt | 88.0 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.257× (z -13.2) |
| [[A549 (line)]] | wt | 46.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.401× (z -10.4) |
| [[AN3 CA (line)]] | alt | 69.1 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0663× (z -12.3) |
| [[HT-29 (line)]] | alt | 106 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.278× (z -10.7) |
| [[A-427 (line)]] | wt | 64.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.322× (z -13.3) |
| [[H4 (line)]] | wt | 39.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.239× (z -9.7) |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.395× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 55.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.359× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 67.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 32.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -10.5) |
| [[RKO (line)]] | wt | 60.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.355× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0630× (z -15.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MASTL]] | +0.85 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[ZNF724]] | +0.84 | +0.81 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[ESCO2]] | +0.84 | +0.87 / +0.81 | both halves | 7e-06 | STRING 480 |
| [[CIP2A]] | +0.81 | +0.84 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[GEN1]] | +0.81 | +0.86 / +0.79 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 796 |
| [[FAM111A]] | +0.78 | +0.80 / +0.78 | both halves | 7e-06 |  |
| [[SGO1]] | +0.78 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[KIF24]] | +0.77 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[BRIP1]] | +0.77 | +0.78 / +0.78 | both halves | 7e-06 | same gene group; pathway: DNA Double-Strand Break Repair; STRING 998 |
| [[USP1]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 605 |
| [[BRCA1]] | +0.76 | +0.75 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[FANCD2]] | +0.75 | +0.76 / +0.75 | both halves | 7e-06 | same gene group; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises BRCA2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.29× lower at baseline in the lines without E2F8 | 0.039 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises BRCA2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without FAM111B | 0.077 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[C5]] | C | C5 activity raises BRCA2's level | lines that do not express C5 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without C5 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLSPN, PRDM6, TCF19; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises BRCA2's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.54× lower at baseline in the lines without SKA3 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRN3]] | B | BRCA2 activity strengthens LRRN3's drug response | recorded loss-of-function mutation of BRCA2 in 6 lines vs 30 not recorded | the BRCA2-altered lines respond the other way (z diff +1.87); strongest at Dinaciclib 0.5 µM: 0.31x vs 2.22x (z diff +6.4) | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.886). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-40.8, -47.8); signed map (-43.7, -47.4). **Vector** length 147, 50.4% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.6 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.7 | +5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +0.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.9 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.9 | -9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.8 | -9.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.4 | -6.7 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.1 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -6.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BRCA2 DNA repair associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q13.1 — chr13:32,315,086-32,400,268 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAD, FAD1, BRCC2, XRCC11; previously FANCD1, FACD, FANCD |
| Gene groups (HGNC) | FA complementation groups |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 24 pathways, smallest: HDR through MMEJ (alt-NHEJ); Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [P51587](https://www.uniprot.org/uniprotkb/P51587) (Breast cancer type 2 susceptibility protein):

> Tumor suppressor protein that maintains genome stability primarily by repairing damaged DNA through homologous recombination (HR). Facilitates the repair of double-strand breaks (DSBs) by binding and mediating the loading of the RAD51 protein onto single-stranded DNA (ssDNA), thereby promoting the activity of RAD51, which catalyzes DNA strand exchange. BRCA2 nucleates and stabilizes RAD51 on ssDNA directly and delivers RAD51 to ssDNA-double-stranded DNA (dsDNA) junctions by sliding along dsDNA …

**Summary**, from NCBI Gene [675](https://www.ncbi.nlm.nih.gov/gene/675):

> The product of this gene in involved in maintenance of genome stability. It is involved in double-strand break repair pathways during mitotic and meiotic homologous recombination and functions in protecting DNA replication forks. The encoded protein contains sites for interactions with PALB2 and EMSY and an N-terminal DNA binding domain. It also contains a RAD51 binding domain with multiple components. It has multiple BRC repeats, an alpha helix domain, oligonucleotide binding folds, and a …

**Accessions** — [HGNC:1101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1101) · Entrez [675](https://www.ncbi.nlm.nih.gov/gene/675) · UniProt [P51587](https://www.uniprot.org/uniprotkb/P51587) · Ensembl [ENSG00000139618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139618)

## Data

Gene col 6320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6320); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6320]; `tensor/DDL_lfc|DDL_z.npy` [6320]; `embed/gene_vectors.npy` [6320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6320 or target_col == 6320). Every well: [[BRCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/BRCA2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

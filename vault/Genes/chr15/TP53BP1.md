---
symbol: "TP53BP1"
type: "gene"
col: 861
ensembl_id: "ENSG00000067369"
name: "tumor protein p53 binding protein 1"
location: "15q15.3"
module: 64
arm: "+"
pooled_cpm: 125.62
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/064", "written"]
generated_by: "tahoemap"
---

# TP53BP1

*tumor protein p53 binding protein 1* — 15q15.3

> [!summary] In one line
> TP53BP1 encodes 53BP1, a chromatin adaptor that reads the histone marks around a double-strand break and steers repair toward end-joining — named for a p53 interaction that is still the least settled thing about it.

## What it is

53BP1 is a large, mostly scaffold-like protein with no catalytic activity. It was isolated in a two-hybrid screen as a protein binding wild-type but not mutant p53, through tandem C-terminal BRCT domains that contact the p53 core domain — hence the name. Its principal characterised job, however, is in double-strand break repair. Nucleosomes flanking a break carry constitutive H4K20me2 and, after RNF168 acts, H2A Lys15 ubiquitylation; 53BP1 reads both simultaneously, with its tandem Tudor domain on the methyl mark and a short ubiquitylation-dependent recruitment motif on the ubiquitin, which is why it concentrates into the microscopically visible foci that define a damaged nucleus. ATM then phosphorylates its N-terminal SQ/TQ cluster, creating a platform for RIF1 and the shieldin complex, which blocks CtIP, MRE11 and EXO1 from resecting the break ends. The consequence is pathway choice: 53BP1 protects ends for non-homologous end joining and suppresses homologous recombination. That logic is the basis of one of the cleanest genetic interactions in the field — loss of 53BP1 restores recombination and viability to BRCA1-deficient cells and is a recognised route to PARP-inhibitor resistance. Mouse knockouts show DNA-damage-response defects, impaired class switch recombination and tumour susceptibility, and 53BP1 behaves as a haploinsufficient tumour suppressor cooperating with p53. The p53 connection has been revisited more recently: 53BP1 does promote p53-dependent transcription and cell-fate decisions, through a mechanism separable from its repair function.

## What is uncertain

The interaction the gene is named for is the weakest-supported part of its biology. Whether BRCT-mediated p53 binding contributes meaningfully to p53 activity in cells, as opposed to being a detectable affinity, has never been settled; the more recent evidence for a 53BP1 contribution to p53-dependent transcription points to a different, oligomerisation- and chromatin-dependent mechanism, and rests on a limited number of systems. Separately, 53BP1 mRNA is a poor proxy for 53BP1 function: recruitment depends on H4K20me2 density, RNF168 activity, ATM phosphorylation and competition with BRCA1-associated factors, none of which move with the transcript. Its effect on repair outcome is also strongly context-dependent — pro-survival in some settings, actively deleterious in BRCA1-mutant cells.

## References

- Iwabuchi et al., 1994, PNAS — identified two proteins binding wild-type but not mutant p53, one of which became 53BP1.
- Schultz et al., 2000, Journal of Cell Biology — placed 53BP1 as an early participant in the cellular response to double-strand breaks.
- Botuyan et al., 2006, Cell — structural basis for methylation-state-specific recognition of H4K20me2 by the 53BP1 Tudor domain.
- Bunting et al., 2010, Cell — 53BP1 inhibits homologous recombination in Brca1-deficient cells by blocking end resection.
- Fradet-Turcotte et al., 2013, Nature — 53BP1 is a reader of the damage-induced H2A Lys15 ubiquitin mark.
- Cuella-Martin et al., 2016, Molecular Cell — separated 53BP1's DNA-repair and p53-dependent cell-fate functions mechanistically.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.71× (z +13.9, q 7e-41, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -9.6, q 5e-19, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BNIP1]] (+0.62, fdr 1e-05), [[NDUFA5]] (+0.61, fdr 1e-05), [[BTN3A1]] (+0.60, fdr 1e-05); moves opposite to [[SNTB2]] (-0.57, fdr 1e-05), [[KLHL29]] (-0.54, fdr 1e-05), [[DOCK9]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +13.9 | 7e-41 | 41/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.9 | 9e-13 | 34/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +6.8 | 1e-09 | 39/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.2 | 8e-08 | 37/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.37×** | +5.5 | 4e-06 | 29/48 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +4.6 | 4e-04 | 29/48 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.014 | 25/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.23×** | +3.7 | 0.015 | 24/48 (LOX-IMVI, SW480, …) | two highest doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.15× | +3.5 | 0.029 | 8/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.059 | 21/48 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.10 | 15/48 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +3.0 | 0.12 | 18/48 (C32, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -9.6 | 5e-19 | 40/49 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.633×** | -8.3 | 2e-14 | 40/49 (NCI-H1792, SNU-1, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -7.2 | 1e-10 | 38/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.670×** | -6.8 | 2e-09 | 32/45 (A549, CFPAC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.681×** | -6.7 | 2e-09 | 34/44 (C-33 A, hTERT-HPNE, …) | all doses, flat | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -6.3 | 4e-08 | 39/50 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.798×** | -4.0 | 0.006 | 28/47 (RKO, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -3.3 | 0.059 | 17/48 (A498, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 144 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[NCI-H460 (line)]] | wt | 110 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.9) |
| [[PANC-1 (line)]] | alt | 152 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -12.0) |
| [[A498 (line)]] | wt | 219 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -19.0) |
| [[A-172 (line)]] | wt | 150 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +19.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 173 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 183 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.3) |
| [[RKO (line)]] | wt | 106 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -20.8) ⚠ toxic; cell-cycle shift, explains ~22% of this change |
| [[SNU-1 (line)]] | wt | 134 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.7) |
| [[A549 (line)]] | wt | 98.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 162 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[H4 (line)]] | wt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 147 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) | [[Belzutifan (drug)]] 5 µM 0.151× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 139 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 65.4 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 205 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 138 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 72.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 103 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.590× (z -8.9) |
| [[A-427 (line)]] | wt | 83.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.2) | — |
| [[AN3 CA (line)]] | alt | 203 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -21.0) |
| [[AsPC-1 (line)]] | alt | 87.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.4) |
| [[C32 (line)]] | wt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HepG2_C3A (line)]] | wt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 93.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -13.7) |
| [[HS-578T (line)]] | alt | 98.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -8.7) |
| [[HT-29 (line)]] | alt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.2) | — |
| [[LoVo (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +21.8) | — |
| [[RPMI-7951 (line)]] | alt | 201 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.5) | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.2) | — |
| [[SW 1271 (line)]] | alt | 124 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.144× (z -9.6) |
| [[SW 900 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.444× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.8) | — |
| [[SW480 (line)]] | alt | 104 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 102 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BNIP1]] | +0.62 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[NDUFA5]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BTN3A1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.60 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[VIRMA]] | +0.60 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[NPHP1]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CREB3]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[INTU]] | +0.58 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[EDC3]] | +0.55 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[AAAS]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[RBSN]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNTB2]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[KLHL29]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[DOCK9]] | -0.53 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[STK39]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[SRPK1]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[TMEM164]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[FAM135A]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[TAF4]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[PTPN12]] | -0.49 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HDAC4]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 | pathway: SUMO E3 ligases SUMOylate target proteins; STRING 873 |
| [[TSPAN14]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CHD7]] | -0.48 | -0.49 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TP53BP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ARMCX1]] | B | ARMCX1 activity raises TP53BP1's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without ARMCX1 | 0.064 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[BRSK1]] | B | BRSK1 activity raises TP53BP1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without BRSK1 | 0.069 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-23.1, 1.9); signed map (-13.9, -10.3). **Vector** length 99.8, 30.5% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +13.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.9 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +4.5 | -8.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.3 | +0.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.2 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -0.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p53 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,403,061-43,510,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 53BP1, p202, TDRD30 |
| Gene groups (HGNC) | Tudor domain containing |
| Reactome | 15 pathways, smallest: SUMOylation of transcription factors; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12888](https://www.uniprot.org/uniprotkb/Q12888) (TP53-binding protein 1):

> Double-strand break (DSB) repair protein involved in response to DNA damage, telomere dynamics and class-switch recombination (CSR) during antibody genesis. Plays a key role in the repair of double-strand DNA breaks (DSBs) in response to DNA damage by promoting non-homologous end joining (NHEJ)-mediated repair of DSBs and specifically counteracting the function of the homologous recombination (HR) repair protein BRCA1. In response to DSBs, phosphorylation by ATM promotes interaction with RIF1 …

**Summary**, from NCBI Gene [7158](https://www.ncbi.nlm.nih.gov/gene/7158):

> This gene encodes a protein that functions in the DNA double-strand break repair pathway choice, promoting non-homologous end joining (NHEJ) pathways, and limiting homologous recombination. This protein plays multiple roles in the DNA damage response, including promoting checkpoint signaling following DNA damage, acting as a scaffold for recruitment of DNA damage response proteins to damaged chromatin, and promoting NHEJ pathways by limiting end resection following a double-strand break. These …

**Accessions** — [HGNC:11999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11999) · Entrez [7158](https://www.ncbi.nlm.nih.gov/gene/7158) · UniProt [Q12888](https://www.uniprot.org/uniprotkb/Q12888) · Ensembl [ENSG00000067369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067369)

## Data

Gene col 861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 861); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 861]; `tensor/DDL_lfc|DDL_z.npy` [861]; `embed/gene_vectors.npy` [861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 861 or target_col == 861). Every well: [[TP53BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TP53BP1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

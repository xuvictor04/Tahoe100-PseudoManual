---
symbol: "SLC7A5"
type: "gene"
col: 2345
ensembl_id: "ENSG00000103257"
name: "solute carrier family 7 member 5"
location: "16q24.2"
module: 63
arm: "+"
pooled_cpm: 94.08
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SLC7A5

*solute carrier family 7 member 5* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.87× (z +7.7, q 1e-11, up in 42 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.84× (z +7.5, q 2e-11, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.640× (z -5.5, q 2e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AARS1]] (+0.68, fdr 7e-06), [[ASNS]] (+0.67, fdr 7e-06), [[SLC1A4]] (+0.66, fdr 7e-06); moves opposite to [[ZNF214]] (-0.49, fdr 5e-05), [[KIAA1586]] (-0.48, fdr 3e-05), [[WBP4]] (-0.45, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2345.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +7.7 | 1e-11 | 42/48 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +7.5 | 2e-11 | 40/48 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +7.4 | 2e-11 | 42/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +5.6 | 3e-06 | 31/49 (H4, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.28×** | +5.3 | 2e-05 | 31/47 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.35×** | +5.2 | 2e-05 | 32/48 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.49×** | +4.9 | 9e-05 | 30/48 (HOP62, HCT15, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.6 | 3e-04 | 29/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 27/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.87×** | +4.0 | 0.003 | 25/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.011 | 26/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.012 | 22/48 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.021 | 22/48 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.021 | 24/49 (MIA PaCa-2, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.028 | 21/48 (A498, HepG2/C3A, …) | top dose only |  |
| [[Encorafenib (drug)]] 5 µM |  | **1.66×** | +3.2 | 0.041 | 23/48 (Hs 766T, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.046 | 20/48 (NCI-H2030, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2345.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -5.5 | 2e-05 | 30/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.633×** | -5.2 | 5e-05 | 34/47 (NCI-H2347, RKO, …) | all doses, flat | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.697×** | -4.3 | 0.003 | 25/48 (LoVo, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.796×** | -4.0 | 0.009 | 22/48 (SNU-1, SW1417, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.606× | -3.2 | 0.14 | 20/47 (LoVo, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2345. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 152 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -17.2) |
| [[CHP-212 (line)]] | wt | 111 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0162× (z -21.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0933× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 47.9 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.14× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 105 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.311× (z -11.8) |
| [[A-172 (line)]] | wt | 153 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 28.8 | 3 (2 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.61× (z +8.9) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 4.51× (z +8.8) | — |
| [[RKO (line)]] | wt | 80.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -11.0) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 167 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.223× (z -11.0) |
| [[HOP62 (line)]] | alt | 56.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.14× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.92× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 40.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.53× (z +10.3) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 87.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 180 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +15.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 61.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 94.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 148 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.304× (z -10.5) |
| [[LS 180 (line)]] | wt | 81.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.279× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0527× (z -11.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 80.1 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.345× (z -9.2) |
| [[A549 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 223 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 112 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 134 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 98.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2345), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AARS1]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ASNS]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 848 |
| [[SLC1A4]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY; STRING 671 |
| [[PHGDH]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PSAT1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 542 |
| [[IARS1]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[MTHFD2]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 561 |
| [[CHAC1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 406 |
| [[HSPA9]] | +0.63 | +0.58 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PYCR1]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 | pathway: Metabolism of amino acids and derivatives |
| [[MARS1]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 | same gene group; pathway: Metabolism of amino acids and derivatives |
| [[SLC1A5]] | +0.61 | +0.57 / +0.60 | both halves | 8e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 885 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF214]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[KIAA1586]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[WBP4]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[GPATCH8]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.1, 48.2); signed map (-14.0, 25.2). **Vector** length 143, 47.4% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.57 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.57 to 9); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.1 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.4 | -0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.2 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.9 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.8 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.8 | -5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.2 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.2 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,830,023-87,869,507 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LAT1, E16, D16S469E, MPE16, CD98 |
| Gene groups (HGNC) | CD molecules; MicroRNA protein coding host genes; Solute carrier family 7 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING, G2M_CHECKPOINT |
| Reactome | 9 pathways, smallest: Tryptophan catabolism; Basigin interactions; Amino acid transport across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01650](https://www.uniprot.org/uniprotkb/Q01650) (Large neutral amino acids transporter small subunit 1):

> Forms a heterodimer with SLC3A2 that functions as a sodium-independent transporter for large neutral amino acids. Functions as an obligatory amino acid antiporter, mediating the exchange of amino acids and amino acid-related compounds across the plasma membrane. Also mediates sodium-independent exchange of iodothyronines with neutral and aromatic L-alpha-amino acids. Mediates exchange of L-tryptophan with the tryptophan metabolites L-kynurenine and 3-hydroxy-L-kynurenine. Mediates cellular …

**Summary**, from NCBI Gene [8140](https://www.ncbi.nlm.nih.gov/gene/8140):

> Enables transmembrane transporter activity. Involved in carboxylic acid transport; thyroid hormone transport; and xenobiotic transport. Located in apical plasma membrane; cytosol; and microvillus membrane. Part of amino acid transport complex. Implicated in cholangiocarcinoma; colon cancer; hepatocellular carcinoma; and lung squamous cell carcinoma. Biomarker of esophagitis; gastrointestinal system cancer (multiple); malignant astrocytoma (multiple); and respiratory system cancer (multiple). …

**Accessions** — [HGNC:11063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11063) · Entrez [8140](https://www.ncbi.nlm.nih.gov/gene/8140) · UniProt [Q01650](https://www.uniprot.org/uniprotkb/Q01650) · Ensembl [ENSG00000103257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103257)

## Data

Gene col 2345: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2345); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2345, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2345]; `tensor/DDL_lfc|DDL_z.npy` [2345]; `embed/gene_vectors.npy` [2345]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2345 or target_col == 2345). Every well: [[SLC7A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

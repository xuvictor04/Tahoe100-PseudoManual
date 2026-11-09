---
symbol: "PIGG"
type: "gene"
col: 10474
ensembl_id: "ENSG00000174227"
name: "phosphatidylinositol glycan anchor biosynthesis class G (EMM blood group)"
location: "4p16.3"
module: 52
arm: "+"
pooled_cpm: 55.0
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PIGG

*phosphatidylinositol glycan anchor biosynthesis class G (EMM blood group)* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.86× (z +4.9, q 4e-04, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.592× (z -7.7, q 6e-12, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.779× (z -5.4, q 5e-06, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACAD9]] (+0.73, fdr 2e-05), [[PDCD6]] (+0.71, fdr 7e-06), [[RECQL5]] (+0.69, fdr 7e-06); moves opposite to [[HPF1]] (-0.58, fdr 1e-05), [[TTBK2]] (-0.58, fdr 1e-05), [[MIER1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +4.9 | 4e-04 | 31/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.006 | 21/48 (SW 900, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +4.2 | 0.006 | 29/48 (KATO III, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.26× | +3.4 | 0.11 | 24/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.592×** | -7.7 | 6e-12 | 39/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -7.3 | 9e-11 | 37/47 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.647×** | -6.7 | 4e-09 | 35/49 (NCI-H1573, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.649×** | -6.1 | 1e-07 | 27/45 (LoVo, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.760×** | -6.0 | 3e-07 | 31/48 (NCI-H1792, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -5.4 | 5e-06 | 34/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -5.2 | 1e-05 | 31/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.716×** | -5.1 | 2e-05 | 33/48 (SW1417, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.720×** | -4.9 | 8e-05 | 25/42 (LS 180, HT-29, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.743×** | -4.6 | 3e-04 | 33/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.744×** | -4.5 | 3e-04 | 27/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -3.5 | 0.023 | 20/48 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 79.0 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 66.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -9.0) |
| [[A498 (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.418× (z -8.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 53.9 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.134× (z -9.4) |
| [[H4 (line)]] | wt | 96.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HCT15 (line)]] | alt | 52.5 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0640× (z -9.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HepG2_C3A (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.2) ⚠ cell-cycle shift, explains ~92% of this change |
| [[KATO III (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LS 180 (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 49.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[NCI-H460 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.350× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[RPMI-7951 (line)]] | alt | 53.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 56.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAD9]] | +0.73 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[PDCD6]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[RECQL5]] | +0.69 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[MAEA]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PMM2]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[MAP3K7]] | +0.65 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[SPTLC1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[DCTN5]] | +0.65 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[FUBP3]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF26]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[HCG18]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[CHFR]] | +0.64 | +0.62 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TTBK2]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[MIER1]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[GKAP1]] | -0.55 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TSPAN15]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CYRIA]] | -0.55 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CDC73]] | -0.55 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[HMGN3]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[PIM3]] | -0.53 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[MAP4K5]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[LINC01273]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[HSF2]] | -0.52 | -0.46 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.1, 0.7); signed map (-48.3, 1.2). **Vector** length 97.8, 24.5% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +4.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -5.7 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.6 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.1 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol glycan anchor biosynthesis class G (EMM blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:499,210-540,200 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20265, GPI7, LAS21 |
| Gene groups (HGNC) | Blood group antigens; Phosphatidylinositol glycan anchor biosynthesis |
| Reactome | 2 pathways, smallest: Synthesis of glycosylphosphatidylinositol (GPI); Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5H8A4](https://www.uniprot.org/uniprotkb/Q5H8A4) (GPI ethanolamine phosphate transferase 2, catalytic subunit):

> Catalytic subunit of the ethanolamine phosphate transferase 2 complex that transfers an ethanolamine phosphate (EtNP) from a phosphatidylethanolamine (PE) to the 6-OH position of the second alpha-1,6-linked mannose of a 2-acyl-6-[6-phosphoethanolamine-alpha-D-mannosyl-(1->2)-alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H7) intermediate to generate a …

**Summary**, from NCBI Gene [54872](https://www.ncbi.nlm.nih.gov/gene/54872):

> This gene encodes an enzyme involved in glycosylphosphatidylinositol-anchor biosynthesis. The encoded protein, which is localized to the endoplasmic reticulum, is involved in transferring ethanoloamine phosphate to mannose 2 of glycosylphosphatidylinositol species H7 to form species H8. Allelic variants of this gene have been associated with intellectual disability, hypotonia, and early-onset seizures. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:25985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25985) · Entrez [54872](https://www.ncbi.nlm.nih.gov/gene/54872) · UniProt [Q5H8A4](https://www.uniprot.org/uniprotkb/Q5H8A4) · Ensembl [ENSG00000174227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174227)

## Data

Gene col 10474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10474); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10474]; `tensor/DDL_lfc|DDL_z.npy` [10474]; `embed/gene_vectors.npy` [10474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10474 or target_col == 10474). Every well: [[PIGG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIGG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

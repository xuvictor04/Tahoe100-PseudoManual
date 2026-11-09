---
symbol: "MIB2"
type: "gene"
col: 12411
ensembl_id: "ENSG00000197530"
name: "MIB E3 ubiquitin protein ligase 2"
location: "1p36.33"
module: 157
arm: "+"
pooled_cpm: 8.91
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# MIB2

*MIB E3 ubiquitin protein ligase 2* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.74× (z +6.7, q 1e-08, up in 8 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +4.9, q 1e-04, up in 18 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.525× (z -8.1, q 4e-13, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIDD1]] (+0.64, fdr 1e-05), [[RPS6KB2]] (+0.62, fdr 1e-05), [[ZFPL1]] (+0.61, fdr 1e-05); moves opposite to [[GLO1]] (-0.64, fdr 7e-06), [[CCT5]] (-0.54, fdr 1e-05), [[PTGES3]] (-0.53, fdr 1e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.7 | 1e-08 | 8/18 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +6.4 | 3e-08 | 17/35 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.8 | 1e-06 | 19/38 (J82, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +5.1 | 5e-05 | 11/24 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.9 | 1e-04 | 18/44 (A549, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.8 | 1e-04 | 20/44 (Hs 766T, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.016 | 13/43 (RPMI-7951, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.069 | 8/48 (SW480, SNU-1, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.077 | 10/41 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.27× | +3.0 | 0.15 | 8/44 (LoVo, RPMI-7951, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.525×** | -8.1 | 4e-13 | 32/47 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -7.2 | 2e-10 | 27/48 (AsPC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -6.0 | 4e-07 | 25/47 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.621×** | -5.6 | 2e-06 | 23/45 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.453×** | -5.2 | 2e-05 | 24/46 (J82, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -5.0 | 4e-05 | 22/46 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -5.0 | 4e-05 | 21/46 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -5.0 | 5e-05 | 21/45 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.674×** | -4.9 | 5e-05 | 17/45 (SNU-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -4.9 | 6e-05 | 22/44 (AsPC-1, SW48, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.669×** | -4.8 | 6e-05 | 20/46 (AsPC-1, HCT15, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.6 | 2e-04 | 20/46 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.507×** | -4.4 | 4e-04 | 16/34 (Hs 766T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -3.8 | 0.006 | 17/48 (HCT15, MIA PaCa-2, …) | two highest doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.5 µM |  | **0.758×** | -3.5 | 0.020 | 5/48 (SW 1271, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Talc (drug)]] 0.05 µM |  | **0.762×** | -3.4 | 0.024 | 16/46 (PANC-1, SHP-77, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.597×** | -3.4 | 0.024 | 14/42 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.040 | 14/45 (RPMI-7951, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.07 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0713× (z -8.7) |
| [[COLO 205 (line)]] | alt | 9.58 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.111× (z -8.7) |
| [[H4 (line)]] | wt | 13.0 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0763× (z -9.8) |
| [[HT-29 (line)]] | alt | 9.88 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.159× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.122× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.147× (z -8.6) |
| [[SHP-77 (line)]] | alt | 6.87 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.106× (z -8.9) |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.39 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIDD1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[RPS6KB2]] | +0.62 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[ZFPL1]] | +0.61 | +0.50 / +0.69 | both halves | 1e-05 | same gene group |
| [[GSK3A]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[MGRN1]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DGAT1]] | +0.58 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CCNL2]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[GET4]] | +0.58 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KLC4]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[FBRS]] | +0.57 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CDK5RAP3]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FDXR]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLO1]] | -0.64 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[CCT5]] | -0.54 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[PTGES3]] | -0.53 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.50 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SNX10]] | -0.50 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[HSP90AA1]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[HSPD1]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-13.8, -26.0); signed map (-10.3, 4.5). **Vector** length 65.7, 10.2% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.4 | +5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +2.2 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -8.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MIB E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,615,454-1,630,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | skeletrophin, ZZZ5, FLJ39787; previously ZZANK1 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers ZZ-type; Ankyrin repeat domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 27 pathways, smallest: Constitutive Signaling by NOTCH1 HD Domain Mutants; Signaling by NOTCH1 HD Domain Mutants in Cancer; PD-L1(CD274) glycosylation and translocation to plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AX9](https://www.uniprot.org/uniprotkb/Q96AX9) (E3 ubiquitin-protein ligase MIB2):

> E3 ubiquitin-protein ligase that mediates ubiquitination of Delta receptors, which act as ligands of Notch proteins. Positively regulates the Delta-mediated Notch signaling by ubiquitinating the intracellular domain of Delta, leading to endocytosis of Delta receptors.

**Summary**, from NCBI Gene [142678](https://www.ncbi.nlm.nih.gov/gene/142678):

> The protein encoded by this gene is an E3 ubiquitin protein ligase that mediates ubiquitination of proteins in the Notch signaling pathway. The encoded protein may be a suppressor of melanoma invasion. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:30577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30577) · Entrez [142678](https://www.ncbi.nlm.nih.gov/gene/142678) · UniProt [Q96AX9](https://www.uniprot.org/uniprotkb/Q96AX9) · Ensembl [ENSG00000197530](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197530)

## Data

Gene col 12411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12411); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12411]; `tensor/DDL_lfc|DDL_z.npy` [12411]; `embed/gene_vectors.npy` [12411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12411 or target_col == 12411). Every well: [[MIB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

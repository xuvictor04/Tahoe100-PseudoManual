---
symbol: "SRPRB"
type: "gene"
col: 6940
ensembl_id: "ENSG00000144867"
name: "SRP receptor subunit beta"
location: "3q22.1"
module: 49
arm: "+"
pooled_cpm: 29.67
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SRPRB

*SRP receptor subunit beta* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.73× (z +6.6, q 1e-08, up in 21 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.69× (z +6.6, q 1e-08, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.760× (z -5.0, q 2e-04, down in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 0.386×, AsPC-1 0.226×, RPMI-7951 0.257×, HS-578T 0.350×, …); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.395×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM98A]] (+0.72, fdr 7e-06), [[TRIM27]] (+0.72, fdr 7e-06), [[NFXL1]] (+0.72, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6940.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.73×** | +6.6 | 1e-08 | 21/37 (NCI-H1792, SNU-423, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.6 | 1e-08 | 29/47 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +6.0 | 3e-07 | 30/48 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.57×** | +5.7 | 2e-06 | 27/44 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.2 | 3e-05 | 27/48 (NCI-H1573, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.0 | 6e-05 | 29/46 (NCI-H1573, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.7 | 2e-04 | 4/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.03×** | +4.7 | 2e-04 | 27/48 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.6 | 3e-04 | 30/48 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.62×** | +4.3 | 8e-04 | 26/48 (MIA PaCa-2, LoVo, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.003 | 22/48 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.005 | 21/48 (LoVo, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.005 | 21/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.007 | 18/46 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +3.7 | 0.007 | 16/48 (SW1417, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.6 | 0.010 | 17/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.70×** | +3.5 | 0.016 | 17/48 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.4 | 0.019 | 20/48 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +3.3 | 0.025 | 17/47 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.030 | 14/48 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6940.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 0.386×, AsPC-1 0.226×, RPMI-7951 0.257×, HS-578T 0.350×, …); [[Panobinostat (drug)]] 5 µM in 1 line (A498 0.395×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.760×** | -5.0 | 2e-04 | 27/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.761×** | -4.9 | 2e-04 | 24/48 (LS 180, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.773× | -3.3 | 0.15 | 14/47 (PANC-1, CFPAC-1, …) | two highest doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.767× | -3.3 | 0.15 | 18/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.783× | -3.1 | 0.16 | 12/48 (HT-29, LS 180, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.785× | -3.1 | 0.16 | 11/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -3.1 | 0.16 | 18/48 (A498, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6940. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 93.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 22.2 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 5.66× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 22.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.5) |
| [[COLO 205 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.26× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.7) |
| [[J82 (line)]] | alt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 27.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -12.8) |
| [[SW480 (line)]] | alt | 28.3 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.96× (z +10.2) | — |
| [[A-172 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6940), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM98A]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[TRIM27]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[NFXL1]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[GORASP2]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[SSR3]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 631 |
| [[COG3]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[HM13]] | +0.67 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[ARL1]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[GMPPA]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[OSTC]] | +0.65 | +0.63 / +0.58 | both halves | 8e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 414 |
| [[SLC33A1]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -33.9); signed map (-53.4, 10.5). **Vector** length 108, 29.7% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +6.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +5.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.5 | +3.9 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.5 | +4.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | SRP receptor subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,784,023-133,825,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APMCF1, SR-beta |
| Gene groups (HGNC) | Signal recognition particle GTPases |
| Hallmark sets | PANCREAS_BETA_CELLS, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 7 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5M8](https://www.uniprot.org/uniprotkb/Q9Y5M8) (Signal recognition particle receptor subunit beta):

> Component of the signal recognition particle (SRP) complex receptor (SR) (By similarity). Ensures, in conjunction with the SRP complex, the correct targeting of the nascent secretory proteins to the endoplasmic reticulum membrane system (By similarity). May mediate the membrane association of SR (By similarity).

**Summary**, from NCBI Gene [58477](https://www.ncbi.nlm.nih.gov/gene/58477):

> The protein encoded by this gene has similarity to mouse protein which is a subunit of the signal recognition particle receptor (SR). This subunit is a transmembrane GTPase belonging to the GTPase superfamily. It anchors alpha subunit, a peripheral membrane GTPase, to the ER membrane. SR is required for the cotranslational targeting of both secretory and membrane proteins to the ER membrane. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24085) · Entrez [58477](https://www.ncbi.nlm.nih.gov/gene/58477) · UniProt [Q9Y5M8](https://www.uniprot.org/uniprotkb/Q9Y5M8) · Ensembl [ENSG00000144867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144867)

## Data

Gene col 6940: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6940); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6940, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6940]; `tensor/DDL_lfc|DDL_z.npy` [6940]; `embed/gene_vectors.npy` [6940]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6940 or target_col == 6940). Every well: [[SRPRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRPRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

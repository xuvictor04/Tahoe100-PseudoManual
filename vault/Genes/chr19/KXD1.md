---
symbol: "KXD1"
type: "gene"
col: 2647
ensembl_id: "ENSG00000105700"
name: "KxDL motif containing 1"
location: "19p13.11"
module: 180
arm: "+"
pooled_cpm: 35.48
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# KXD1

*KxDL motif containing 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +7.4, q 1e-10, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.637× (z -8.6, q 3e-15, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.192×, MIA PaCa-2 0.395×, HEC-1-A 0.466×, HepG2/C3A 0.346×, …); [[Selinexor (drug)]] 5 µM in 2 lines (KATO III 0.416×, RPMI-7951 0.432×; ⚠ cell-cycle shift, explains ~67% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.149×; ⚠ toxic).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZXDC]] (+0.61, fdr 7e-06), [[CDC34]] (+0.60, fdr 1e-05), [[MCRIP1]] (+0.58, fdr 1e-05); moves opposite to [[DHX9]] (-0.56, fdr 1e-05), [[HNRNPM]] (-0.55, fdr 2e-05), [[UTRN]] (-0.52, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2647.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +7.4 | 1e-10 | 37/48 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.1 | 5e-10 | 35/47 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +5.8 | 2e-06 | 30/47 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.4 | 1e-05 | 29/46 (C32, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.7 | 3e-04 | 0/48 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 0.002 | 23/40 (SW 900, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.0 | 0.005 | 29/47 (SNU-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.005 | 26/48 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.006 | 23/48 (NCI-H1792, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.29×** | +3.5 | 0.029 | 22/46 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.085 | 12/48 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.085 | 20/48 (A498, LS 180, …) | two highest doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.085 | 19/46 (SK-MEL-2, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.085 | 16/48 (RKO, SHP-77, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2647.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RKO 0.192×, MIA PaCa-2 0.395×, HEC-1-A 0.466×, HepG2/C3A 0.346×, …); [[Selinexor (drug)]] 5 µM in 2 lines (KATO III 0.416×, RPMI-7951 0.432×; ⚠ cell-cycle shift, explains ~67% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.149×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.637×** | -8.6 | 3e-15 | 36/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.704×** | -4.7 | 6e-04 | 34/47 (RPMI-7951, Hs 766T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Pimozide (drug)]] 5 µM |  | 0.779× | -3.4 | 0.12 | 20/48 (NCI-H2030, NCI-H2347, …) | top dose only | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.774× | -3.3 | 0.12 | 24/47 (C32, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2647. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.149× (z -11.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 41.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 49.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.2) |
| [[KATO III (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.416× (z -8.8) ⚠ cell-cycle shift, explains ~67% of this change |
| [[MIA PaCa-2 (line)]] | alt | 49.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 32.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 40.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.5) | — |
| [[RKO (line)]] | wt | 56.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.432× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2647), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDC]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CDC34]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[GUK1]] | +0.58 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[PRSS53]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[NCKIPSD]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[MAP2K2]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[KYAT1]] | +0.54 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[PPFIA1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[VRK3]] | +0.54 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | -0.56 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPM]] | -0.55 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[UTRN]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SMG7]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ACAA2]] | -0.51 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[ARHGEF9]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[COPS3]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[NAB1]] | -0.50 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HNRNPD]] | -0.50 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PLS3]] | -0.49 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[ASXL1]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[BCLAF1]] | -0.49 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.0, -4.7); signed map (-30.8, 13.1). **Vector** length 77.4, 17.6% of its response variance represented; |z| ≥ 3 in 650 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +3.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -8.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | KxDL motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:18,557,762-18,569,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25480, MGC2749, KXDL, BORCS4; previously C19orf50 |
| Gene groups (HGNC) | BLOC-1 related complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQD3](https://www.uniprot.org/uniprotkb/Q9BQD3) (KxDL motif-containing protein 1):

> As part of the BORC complex may play a role in lysosomes movement and localization at the cell periphery. Associated with the cytosolic face of lysosomes, the BORC complex may recruit ARL8B and couple lysosomes to microtubule plus-end-directed kinesin motor. May be involved in the biogenesis of lysosome-related organelles such as melanosomes (By similarity).

**Summary**, from NCBI Gene [79036](https://www.ncbi.nlm.nih.gov/gene/79036):

> Involved in lysosome localization. Part of BORC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28420) · Entrez [79036](https://www.ncbi.nlm.nih.gov/gene/79036) · UniProt [Q9BQD3](https://www.uniprot.org/uniprotkb/Q9BQD3) · Ensembl [ENSG00000105700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105700)

## Data

Gene col 2647: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2647); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2647, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2647]; `tensor/DDL_lfc|DDL_z.npy` [2647]; `embed/gene_vectors.npy` [2647]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2647 or target_col == 2647). Every well: [[KXD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KXD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

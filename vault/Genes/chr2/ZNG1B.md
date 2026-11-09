---
symbol: "ZNG1B"
type: "gene"
col: 5887
ensembl_id: "ENSG00000136682"
name: "Zn regulated GTPase metalloprotein activator 1B"
location: "2q14.1"
module: 28
arm: "+"
pooled_cpm: 22.72
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZNG1B

*Zn regulated GTPase metalloprotein activator 1B* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +15.0, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 0.734× (z -4.1, q 0.021, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0589×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (A549 0.221×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1A]] (+0.82, fdr 7e-06), [[ZNG1E]] (+0.61, fdr 1e-05), [[UBE2V2]] (+0.60, fdr 1e-05); moves opposite to [[RHEB]] (-0.54, fdr 2e-05), [[RANBP9]] (-0.50, fdr 2e-04), [[PDCL]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +15.0 | 0e+00 | 40/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +12.3 | 3e-32 | 39/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +11.6 | 6e-29 | 19/48 (PANC-1, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +9.0 | 2e-17 | 34/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +8.1 | 7e-14 | 32/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.50×** | +7.5 | 5e-12 | 29/47 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +7.0 | 2e-10 | 23/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +6.6 | 3e-09 | 27/48 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 1e-08 | 25/47 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.3 | 6e-06 | 22/47 (HEC-1-A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +5.3 | 6e-06 | 18/47 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 3e-04 | 17/48 (NCI-H460, SW48, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 9e-04 | 21/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.27×** | +4.2 | 0.001 | 16/43 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +4.2 | 0.001 | 18/47 (SW 900, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 13/47 (NCI-H23, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.003 | 14/48 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.032 | 10/47 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.082 | 7/45 (KATO III, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5887.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0589×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (A549 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.734×** | -4.1 | 0.021 | 16/46 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.827× | -3.6 | 0.10 | 16/44 (Panc 03.27, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.776× | -3.4 | 0.14 | 12/47 (Hs 766T, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +15.6) | — |
| [[A549 (line)]] | wt | 28.1 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.221× (z -9.2) |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0589× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.6) | — |
| [[SW480 (line)]] | alt | 31.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.0) | — |
| [[A-172 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1A]] | +0.82 | +0.85 / +0.76 | both halves | 7e-06 | same gene group; STRING 929 |
| [[ZNG1E]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 | same gene group |
| [[UBE2V2]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MTCH2]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[ZNG1F]] | +0.59 | +0.68 / +0.51 | both halves | 1e-05 | STRING 828 |
| [[GOLGA1]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[GIGYF2]] | +0.55 | +0.73 / +0.39 | both halves | 5e-05 |  |
| [[DMTF1]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[RPAP2]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[PCID2]] | +0.53 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[CHMP4A]] | +0.53 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[AGPAT5]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHEB]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[RANBP9]] | -0.50 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[PDCL]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[LMBRD1]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[NFATC3]] | -0.47 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[LMTK2]] | -0.45 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[MEF2D]] | -0.45 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CUL3]] | -0.45 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PDE5A]] | -0.44 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[KLHDC3]] | -0.44 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CDC42EP4]] | -0.44 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[STRN]] | -0.43 | -0.56 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.9, 17.8); signed map (8.5, -15.5). **Vector** length 68.3, 11.5% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.9 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.1 | +4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Zn regulated GTPase metalloprotein activator 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:113,437,691-113,496,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CBWD2 |
| Gene groups (HGNC) | Zn regulated GTPase metalloprotein activator 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUF1](https://www.uniprot.org/uniprotkb/Q8IUF1) (Zinc-regulated GTPase metalloprotein activator 1B):

> Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them. Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1. After formation of the docked complex, zinc is transferred from the CXCC motif in the GTPase …

**Summary**, from NCBI Gene [150472](https://www.ncbi.nlm.nih.gov/gene/150472):

> Predicted to enable zinc chaperone activity and zinc ion binding activity. Predicted to be involved in protein maturation. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17907) · Entrez [150472](https://www.ncbi.nlm.nih.gov/gene/150472) · UniProt [Q8IUF1](https://www.uniprot.org/uniprotkb/Q8IUF1) · Ensembl [ENSG00000136682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136682)

## Data

Gene col 5887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5887); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5887]; `tensor/DDL_lfc|DDL_z.npy` [5887]; `embed/gene_vectors.npy` [5887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5887 or target_col == 5887). Every well: [[ZNG1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNG1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

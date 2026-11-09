---
symbol: "SLC38A7"
type: "gene"
col: 2308
ensembl_id: "ENSG00000103042"
name: "solute carrier family 38 member 7"
location: "16q21"
module: 172
arm: "+"
pooled_cpm: 11.89
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# SLC38A7

*solute carrier family 38 member 7* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.31× (z +8.4, q 2e-14, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.575× (z -7.9, q 2e-12, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 2 lines (A549 0.0794×, SNU-1 0.102×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.143×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.0835×; ⚠ cell-cycle shift, explains ~49% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.129×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH3]] (+0.76, fdr 7e-06), [[ZFYVE26]] (+0.76, fdr 7e-06), [[WDR81]] (+0.76, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.56, fdr 3e-05), [[TMEM106C]] (-0.55, fdr 4e-05), [[POGLUT2]] (-0.54, fdr 4e-05).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.31×** | +8.4 | 2e-14 | 37/46 (NCI-H460, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +7.4 | 4e-11 | 27/45 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +6.0 | 4e-07 | 8/20 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +5.9 | 6e-07 | 32/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.77×** | +5.4 | 7e-06 | 29/45 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +4.5 | 8e-04 | 24/46 (SK-MEL-2, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.001 | 23/48 (SK-MEL-2, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.2 | 0.002 | 24/41 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.003 | 17/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +4.0 | 0.004 | 20/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.11×** | +3.9 | 0.004 | 13/35 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.006 | 18/48 (NCI-H460, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **2.05×** | +3.8 | 0.007 | 13/44 (NCI-H460, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.008 | 16/47 (NCI-H460, J82, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.010 | 19/47 (LoVo, HepG2/C3A, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.071 | 12/44 (NCI-H460, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.071 | 14/46 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.78×** | +3.0 | 0.075 | 8/42 (SNU-423, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.096 | 13/45 (NCI-H460, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2308.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.05 µM in 2 lines (A549 0.0794×, SNU-1 0.102×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.143×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SNU-423 0.0835×; ⚠ cell-cycle shift, explains ~49% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (C32 0.129×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.575×** | -7.9 | 2e-12 | 42/48 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.514×** | -6.7 | 7e-09 | 34/47 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 25.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 17.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0835× (z -12.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 8.02 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0794× (z -9.9) |
| [[C32 (line)]] | wt | 10.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -9.1) |
| [[Hs 766T (line)]] | wt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +10.3) | — |
| [[J82 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +10.7) | — |
| [[KATO III (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.5) | — |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.190× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 5.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH3]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[WDR81]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[PHYKPL]] | +0.72 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.68 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SLC66A1]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 | STRING 594 |
| [[VPS33A]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[NSMCE2]] | +0.66 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[GUSBP11]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[AP5Z1]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ALG1]] | +0.65 | +0.68 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.56 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[TMEM106C]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[POGLUT2]] | -0.54 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[TFRC]] | -0.53 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[LSM4]] | -0.53 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.855). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-44.9, 11.7); signed map (-8.5, -19.7). **Vector** length 100.0, 22.9% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +4.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.8 | -6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:58,665,109-58,684,770 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10815, SNAT7 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVC3](https://www.uniprot.org/uniprotkb/Q9NVC3) (Sodium-coupled neutral amino acid transporter 7):

> Symporter that selectively cotransports sodium ions and amino acids, such as L-glutamine and L-asparagine from the lysosome into the cytoplasm and may participates in mTORC1 activation. The transport activity requires an acidic lysosomal lumen.

**Summary**, from NCBI Gene [55238](https://www.ncbi.nlm.nih.gov/gene/55238):

> Enables L-asparagine:sodium symporter activity and L-glutamine:sodium symporter activity. Involved in L-glutamine transport and asparagine transport. Located in lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25582) · Entrez [55238](https://www.ncbi.nlm.nih.gov/gene/55238) · UniProt [Q9NVC3](https://www.uniprot.org/uniprotkb/Q9NVC3) · Ensembl [ENSG00000103042](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103042)

## Data

Gene col 2308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2308); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2308]; `tensor/DDL_lfc|DDL_z.npy` [2308]; `embed/gene_vectors.npy` [2308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2308 or target_col == 2308). Every well: [[SLC38A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

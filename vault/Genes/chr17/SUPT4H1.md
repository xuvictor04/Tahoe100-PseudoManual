---
symbol: "SUPT4H1"
type: "gene"
col: 13093
ensembl_id: "ENSG00000213246"
name: "SPT4 homolog, DSIF elongation factor subunit"
location: "17q22"
module: 48
arm: "+"
pooled_cpm: 26.26
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# SUPT4H1

*SPT4 homolog, DSIF elongation factor subunit* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +10.9, q 1e-24, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.642× (z -5.6, q 1e-05, down in 40 of 47 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.179×, LS 180 0.405×, RKO 0.279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.224×, A-427 0.198×); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.250×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNHIT1]] (+0.68, fdr 4e-05), [[ZNF394]] (+0.63, fdr 3e-05), [[WBP1L]] (+0.62, fdr 1e-05); moves opposite to [[SHTN1]] (-0.59, fdr 2e-05), [[TNPO1]] (-0.56, fdr 4e-05), [[DCAF17]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.9 | 1e-24 | 35/47 (HEC-1-A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.68×** | +6.5 | 1e-08 | 39/48 (COLO 205, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.68×** | +6.5 | 1e-08 | 37/48 (SW480, NCI-H460, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.55×** | +5.5 | 4e-06 | 26/45 (C32, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.76×** | +5.5 | 5e-06 | 31/48 (KATO III, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.52×** | +5.3 | 1e-05 | 29/47 (SW480, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.1 | 3e-05 | 28/47 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.3 | 0.001 | 22/45 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.76×** | +4.2 | 0.002 | 25/47 (HCT15, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 23/48 (HOP62, BT-474, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.63×** | +3.6 | 0.018 | 17/46 (COLO 205, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.032 | 20/48 (LoVo, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.035 | 18/45 (SK-MEL-2, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.052 | 12/47 (AsPC-1, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13093.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C-33 A 0.179×, LS 180 0.405×, RKO 0.279×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.224×, A-427 0.198×); [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.357×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.250×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.642×** | -5.6 | 1e-05 | 40/47 (A498, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.0) |
| [[A549 (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 25.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 36.0 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.250× (z -8.6) |
| [[KATO III (line)]] | alt | 41.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 64.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 14.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.2) | — |
| [[RKO (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 45.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.4) | — |
| [[SW48 (line)]] | wt | 63.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -11.2) |
| [[A-172 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 11 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNHIT1]] | +0.68 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[ZNF394]] | +0.63 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[WBP1L]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SYF2]] | +0.62 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DHX8]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MRPL51]] ⚠ | +0.59 | +0.35 / +0.67 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5PF]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 | pathway: Affinity selection of immunoglobulins |
| [[RETREG3]] | +0.57 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[EMC6]] | +0.57 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[ZER1]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NDUFA2]] | +0.57 | +0.40 / +0.56 | both halves | 5e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHTN1]] | -0.59 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[TNPO1]] | -0.56 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[DCAF17]] | -0.55 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[DNAJC10]] | -0.53 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[SSX2IP]] | -0.53 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[OCRL]] | -0.50 | -0.25 / -0.59 | both halves | 4e-04 |  |
| [[OXCT1]] | -0.48 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[RBBP8]] | -0.48 | -0.17 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |
| [[BCAP29]] | -0.47 | -0.26 / -0.53 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-28.4, -10.1); signed map (-4.3, -4.7). **Vector** length 73.0, 16.2% of its response variance represented; |z| ≥ 3 in 611 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.2 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SPT4 homolog, DSIF elongation factor subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:58,345,175-58,353,093 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPT4H, Spt4, Supt4a; previously SUPT4H |
| Hallmark sets | DNA_REPAIR |
| Reactome | 26 pathways, smallest: Abortive elongation of HIV-1 transcript in the absence of Tat; Pausing and recovery of Tat-mediated HIV elongation; Tat-mediated HIV elongation arrest and recovery |
| Matched by | ensembl_id |

**Function**, from UniProt [P63272](https://www.uniprot.org/uniprotkb/P63272) (Transcription elongation factor SPT4):

> Component of the DRB sensitivity-inducing factor complex (DSIF complex), which regulates mRNA processing and transcription elongation by RNA polymerase II. DSIF positively regulates mRNA capping by stimulating the mRNA guanylyltransferase activity of RNGTT/CAP1A. DSIF also acts cooperatively with the negative elongation factor complex (NELF complex) to enhance transcriptional pausing at sites proximal to the promoter. Transcriptional pausing may facilitate the assembly of an elongation …

**Summary**, from NCBI Gene [6827](https://www.ncbi.nlm.nih.gov/gene/6827):

> This gene encodes the small subunit of DRB (5,6-dichloro-1-beta-d-ribofuranosylbenzimidazole) sensitivity-inducing factor (DSIF) complex, which regulates mRNA processing and transcription elongation by RNA polymerase II. The encoded protein is localized to the nucleus and interacts with the large subunit (SUPT5H) to form the DSIF complex. Related pseudogenes have been identified on chromosomes 2 and 12. Alternatively spliced transcript variants have been found for this gene. [provided by …

**Accessions** — [HGNC:11467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11467) · Entrez [6827](https://www.ncbi.nlm.nih.gov/gene/6827) · UniProt [P63272](https://www.uniprot.org/uniprotkb/P63272) · Ensembl [ENSG00000213246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213246)

## Data

Gene col 13093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13093); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13093]; `tensor/DDL_lfc|DDL_z.npy` [13093]; `embed/gene_vectors.npy` [13093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13093 or target_col == 13093). Every well: [[SUPT4H1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUPT4H1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

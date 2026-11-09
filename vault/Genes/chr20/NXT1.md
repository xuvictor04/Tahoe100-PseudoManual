---
symbol: "NXT1"
type: "gene"
col: 5354
ensembl_id: "ENSG00000132661"
name: "nuclear transport factor 2 like export factor 1"
location: "20p11.21"
module: 54
arm: "+"
pooled_cpm: 7.98
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# NXT1

*nuclear transport factor 2 like export factor 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.75× (z +8.3, q 9e-14, up in 41 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.102×, A498 0.220×, NCI-H2347 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0644×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0634×); [[Rimonabant (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0533×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C16orf91]] (+0.65, fdr 4e-05), [[SDHAF1]] (+0.63, fdr 2e-04), [[POP7]] (+0.61, fdr 5e-05); moves opposite to [[UBE2A]] (-0.57, fdr 1e-04), [[UBE2V1]] (-0.53, fdr 0.001, ⚠ one half only (not replicated)), [[PAPOLA]] (-0.53, fdr 4e-04), [[CROCC]] (-0.52, fdr 7e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.75×** | +8.3 | 9e-14 | 41/45 (KATO III, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.97×** | +6.9 | 2e-09 | 27/42 (PANC-1, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.54×** | +6.7 | 4e-09 | 24/41 (SW1417, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.95×** | +6.5 | 1e-08 | 26/37 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +5.5 | 5e-06 | 22/41 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.73×** | +5.3 | 1e-05 | 23/46 (NCI-H1573, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.63×** | +4.9 | 7e-05 | 16/45 (SW480, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +4.9 | 8e-05 | 19/43 (NCI-H1573, SW1417, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.60×** | +4.8 | 1e-04 | 15/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.55×** | +4.5 | 5e-04 | 13/34 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.55×** | +4.4 | 5e-04 | 20/42 (A549, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.52×** | +4.2 | 0.001 | 17/47 (NCI-H1573, NCI-H2347, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.1 | 0.002 | 15/34 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +3.5 | 0.018 | 21/45 (CFPAC-1, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.41×** | +3.5 | 0.018 | 10/47 (PANC-1, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5354.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.102×, A498 0.220×, NCI-H2347 0.156×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Talc (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0644×); [[Tofacitinib (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0634×); [[Rimonabant (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0533×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 0.544× | -3.2 | 0.63 | 6/46 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 9.05 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0644× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 1 | — | [[Rimonabant (drug)]] 0.5 µM 0.0533× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 3.86 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0634× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 5.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 8.37 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0775× (z -8.6) |
| [[SW480 (line)]] | alt | 9.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 7.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 9 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | +0.65 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[SDHAF1]] | +0.63 | +0.32 / +0.69 | both halves | 2e-04 |  |
| [[POP7]] | +0.61 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[TMEM11]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[RPUSD2]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NUDT8]] | +0.59 | +0.31 / +0.61 | both halves | 2e-04 |  |
| [[MRPL14]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.56 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[NCBP2AS2]] | +0.56 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[P3H4]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SNU13]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[NUBP2]] | +0.55 | +0.39 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2A]] | -0.57 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[UBE2V1]] | -0.53 | -0.15 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[PAPOLA]] | -0.53 | -0.26 / -0.53 | both halves | 4e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CROCC]] | -0.52 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[MALAT1]] | -0.51 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[CHMP3]] | -0.51 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CTTN]] | -0.48 | -0.20 / -0.51 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PRKAR1A]] | -0.48 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[MORF4L1P1]] | -0.47 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[LSMEM1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SDCBP]] | -0.47 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SYNJ2BP]] | -0.47 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[PEX19]] | -0.47 | -0.22 / -0.54 | both halves | 6e-04 |  |
| [[PITRM1]] | -0.47 | -0.38 / -0.44 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.7, -12.6); signed map (-34.6, 3.6). **Vector** length 63.8, 11.4% of its response variance represented; |z| ≥ 3 in 755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.0 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +1.7 | +4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +0.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.6 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.5 | -0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transport factor 2 like export factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:23,350,791-23,354,771 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P15, MTR2 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKK6](https://www.uniprot.org/uniprotkb/Q9UKK6) (NTF2-related export protein 1):

> Stimulator of protein export for NES-containing proteins. Also plays a role in the nuclear export of U1 snRNA, tRNA, and mRNA. The NXF1-NXT1 heterodimer is involved in the export of HSP70 mRNA in conjunction with ALYREF/THOC4 and THOC5.

**Summary**, from NCBI Gene [29107](https://www.ncbi.nlm.nih.gov/gene/29107):

> The protein encoded by this gene is located in the nuclear envelope. It has protein similarity to nuclear transport factor 2. This protein functions as a nuclear export factor in both RAN (Ras-related nuclear protein)- and CRM1 (required for chromosome region maintenance)-dependent pathways. It is found to stimulate the export of U1 snRNA in RAN- and CRM1-dependent pathways and the export of tRNA and mRNA in a CRM1-independent pathway. The encoded protein heterodimerizes with Tap protein and …

**Accessions** — [HGNC:15913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15913) · Entrez [29107](https://www.ncbi.nlm.nih.gov/gene/29107) · UniProt [Q9UKK6](https://www.uniprot.org/uniprotkb/Q9UKK6) · Ensembl [ENSG00000132661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132661)

## Data

Gene col 5354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5354); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5354]; `tensor/DDL_lfc|DDL_z.npy` [5354]; `embed/gene_vectors.npy` [5354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5354 or target_col == 5354). Every well: [[NXT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

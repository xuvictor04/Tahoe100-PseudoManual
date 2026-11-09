---
symbol: "ZNG1C"
type: "gene"
col: 12297
ensembl_id: "ENSG00000196873"
name: "Zn regulated GTPase metalloprotein activator 1C"
location: "9q21.11"
module: 5
arm: "+"
pooled_cpm: 5.68
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ZNG1C

*Zn regulated GTPase metalloprotein activator 1C* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.58× (z +5.5, q 2e-05, up in 14 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.45× (z +4.5, q 0.002, up in 4 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.603× (z -5.8, q 3e-06, down in 21 of 43 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.799× (z -3.6, q 0.049, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LoVo 0.160×, SW480 0.173×, J82 0.134×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.192×, A498 0.280×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.152×, J82 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (NCI-H460 0.0754×); [[Ixazomib (drug)]] 0.05 µM in 1 line (A498 0.135×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0762×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1E]] (+0.92, fdr 7e-06), [[ZNG1F]] (+0.76, fdr 7e-06), [[TIMM23B-AGAP6]] (+0.59, fdr 1e-05); moves opposite to [[TAB2]] (-0.54, fdr 3e-05), [[BTD]] (-0.53, fdr 2e-05), [[MTMR3]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12297.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +5.5 | 2e-05 | 14/46 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.5 | 0.002 | 4/46 (SW480, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +3.9 | 0.016 | 8/44 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +3.4 | 0.087 | 0/8 | top dose only | noisy plate (z scaled); position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 1.32× | +3.2 | 0.14 | 5/45 (NCI-H1573, HCT15, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.28× | +3.0 | 0.22 | 5/46 (SHP-77, A549, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12297.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (LoVo 0.160×, SW480 0.173×, J82 0.134×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (C32 0.192×, A498 0.280×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.152×, J82 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[XRK3F2 (drug)]] 0.5 µM in 1 line (NCI-H460 0.0754×); [[Ixazomib (drug)]] 0.05 µM in 1 line (A498 0.135×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (HT-29 0.0762×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.603×** | -5.8 | 3e-06 | 21/43 (A498, C32, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.715×** | -4.0 | 0.016 | 19/41 (KATO III, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **0.729×** | -3.8 | 0.027 | 9/30 (C32, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -3.6 | 0.049 | 13/46 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.812×** | -3.5 | 0.057 | 12/39 (C32, A498, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.754× | -3.1 | 0.16 | 12/14 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[IQ 1 (drug)]] 0.05 µM |  | 0.761× | -3.1 | 0.16 | 3/44 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -3.0 | 0.16 | 7/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12297. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.15 | 0 | 2 (1 ⚠) | — | [[Ixazomib (drug)]] 0.05 µM 0.135× (z -10.0) |
| [[J82 (line)]] | alt | 7.30 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 12.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 4.80 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0762× (z -9.1) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.11 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0754× (z -10.8) |
| [[PANC-1 (line)]] | alt | 4.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12297), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1E]] | +0.92 | +0.89 / +0.87 | both halves | 7e-06 | same gene group |
| [[ZNG1F]] | +0.76 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TIMM23B-AGAP6]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[EXOSC7]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.55 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PUS7]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[RFT1]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TSR1]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[POLR3E]] | +0.52 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[UBE2G2]] | +0.52 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NUP50-DT]] | +0.52 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNG1B]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB2]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[BTD]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MTMR3]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TXNDC16]] | -0.49 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[BMF]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[HDAC5]] | -0.48 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[CRIP2]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CTDSP2]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[RAB30]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PNPLA2]] | -0.47 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TP63]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[PLCL1]] | -0.46 | -0.34 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.6, -41.4); signed map (1.8, -53.9). **Vector** length 52.3, 6.41% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +1.6 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.6 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.4 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Zn regulated GTPase metalloprotein activator 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:68,232,003-68,300,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA561O23.1; previously CBWD3 |
| Gene groups (HGNC) | Zn regulated GTPase metalloprotein activator 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JTY5](https://www.uniprot.org/uniprotkb/Q5JTY5) (Zinc-regulated GTPase metalloprotein activator 1C):

> Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them. Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1. After formation of the docked complex, zinc is transferred from the CXCC motif in the GTPase …

**Summary**, from NCBI Gene [445571](https://www.ncbi.nlm.nih.gov/gene/445571):

> Predicted to enable zinc chaperone activity and zinc ion binding activity. Predicted to be involved in protein maturation. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18519](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18519) · Entrez [445571](https://www.ncbi.nlm.nih.gov/gene/445571) · UniProt [Q5JTY5](https://www.uniprot.org/uniprotkb/Q5JTY5) · Ensembl [ENSG00000196873](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196873)

## Data

Gene col 12297: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12297); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12297, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12297]; `tensor/DDL_lfc|DDL_z.npy` [12297]; `embed/gene_vectors.npy` [12297]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12297 or target_col == 12297). Every well: [[ZNG1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNG1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

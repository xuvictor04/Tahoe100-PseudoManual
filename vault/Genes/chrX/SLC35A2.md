---
symbol: "SLC35A2"
type: "gene"
col: 2214
ensembl_id: "ENSG00000102100"
name: "solute carrier family 35 member A2"
location: "Xp11.23"
module: 56
arm: "+"
pooled_cpm: 10.13
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# SLC35A2

*solute carrier family 35 member A2* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +11.2, q 3e-26, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.744× (z -4.3, q 0.008, down in 15 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.0945×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.235×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.106×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HCT15 0.107×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POFUT2]] (+0.76, fdr 7e-06), [[ARF4]] (+0.72, fdr 7e-06), [[KCNQ1OT1]] (+0.72, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +11.2 | 3e-26 | 25/44 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.7 | 3e-12 | 30/45 (SW480, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.47×** | +5.8 | 1e-06 | 21/48 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +5.5 | 5e-06 | 19/48 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.5 | 5e-06 | 16/38 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.3 | 8e-06 | 16/44 (A498, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +5.2 | 1e-05 | 22/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +4.8 | 1e-04 | 17/48 (SW480, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.27×** | +4.5 | 4e-04 | 18/43 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.34×** | +4.4 | 7e-04 | 13/41 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.34×** | +4.1 | 0.002 | 8/27 (NCI-H460, SNU-423, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.020 | 17/42 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.1 | 0.078 | 1/48 (CHP-212) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | 1.22× | +3.0 | 0.11 | 3/44 (H4, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.0945×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (RPMI-7951 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.235×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (HCT15 0.106×); [[Bimatoprost (drug)]] 0.5 µM in 1 line (HCT15 0.107×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.744×** | -4.3 | 0.008 | 15/43 (RPMI-7951, J82, …) | top dose only | position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | 0.805× | -3.3 | 0.25 | 10/44 (SNU-1, NCI-H1792, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.851× | -3.1 | 0.28 | 7/48 (H4, HCT15, …) | rises with dose |  |
| [[Clotrimazole (drug)]] 0.5 µM |  | 0.817× | -3.1 | 0.28 | 9/44 (SW48, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 12.2 | 0 | 2 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.106× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 7.22 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +8.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.235× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 9.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0945× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 6.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 8.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +8.7) | — |
| [[SW48 (line)]] | wt | 8.55 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0664× (z -8.8) |
| [[A-172 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT2]] | +0.76 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ARF4]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[KCNQ1OT1]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.71 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SURF4]] | +0.71 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[BET1L]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.69 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[COPE]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.69 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.68 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[SPTY2D1]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[TRIM3]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -36.3); signed map (-51.0, 14.3). **Vector** length 62.1, 9.46% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +11.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.0 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +5.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Fluvoxamine (maleate) (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +1.2 | +2.7 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:48,903,180-48,911,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGAT, UGT, UGT1, UGT2, UGTL, UDP-Gal-Tr; previously UGALT |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 6 pathways, smallest: Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [P78381](https://www.uniprot.org/uniprotkb/P78381) (UDP-galactose translocator):

> Transports uridine diphosphate galactose (UDP-galactose) from the cytosol into the Golgi apparatus, functioning as an antiporter that exchanges UDP-galactose for UMP. It is also able to exchange UDP-galactose for AMP and CMP, and to transport UDP-N-acetylgalactosamine (UDP-GalNAc) and other nucleotide sugars. As a provider of UDP-galactose to galactosyltransferases present in the Golgi apparatus, it is necessary for globotriaosylceramide/globoside (Gb3Cer) synthesis from lactosylceramide.

**Summary**, from NCBI Gene [7355](https://www.ncbi.nlm.nih.gov/gene/7355):

> This gene encodes a member of the nucleotide-sugar transporter family. The encoded protein is a multi-pass membrane protein. It transports UDP-galactose from the cytosol into Golgi vesicles, where it serves as a glycosyl donor for the generation of glycans. Mutations in this gene cause congenital disorder of glycosylation type IIm (CDG2M). Multiple alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:11022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11022) · Entrez [7355](https://www.ncbi.nlm.nih.gov/gene/7355) · UniProt [P78381](https://www.uniprot.org/uniprotkb/P78381) · Ensembl [ENSG00000102100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102100)

## Data

Gene col 2214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2214); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2214]; `tensor/DDL_lfc|DDL_z.npy` [2214]; `embed/gene_vectors.npy` [2214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2214 or target_col == 2214). Every well: [[SLC35A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

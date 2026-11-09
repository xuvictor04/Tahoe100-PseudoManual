---
symbol: "ASMTL-AS1"
type: "gene"
col: 14056
ensembl_id: "ENSG00000236017"
name: "ASMTL antisense RNA 1"
location: "Xp22.33 and Yp11.32"
module: 5
arm: "+"
pooled_cpm: 15.32
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ASMTL-AS1

*ASMTL antisense RNA 1* — Xp22.33 and Yp11.32

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.457× (z -6.6, q 2e-08, down in 41 of 47 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Simotinib (drug)]] 0.05 µM: 0.567× (z -4.4, q 0.001, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRWD1]] (+0.68, fdr 7e-06), [[MBD3]] (+0.67, fdr 7e-06), [[LINC00106]] (+0.65, fdr 7e-06, ⚠ same locus), [[PPAN]] (+0.63, fdr 1e-05); moves opposite to [[ANAPC1P2]] (-0.57, fdr 3e-05), [[UBR2]] (-0.56, fdr 1e-05), [[CCNI]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRABD2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14056.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.35× | +3.4 | 0.14 | 17/48 (KATO III, NCI-H2347, …) | rises with dose | position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | 1.35× | +3.4 | 0.14 | 15/48 (HCT15, NCI-H1792, …) | top dose only | position effect removed |
| [[Naproxen (drug)]] 0.05 µM |  | 1.53× | +3.3 | 0.14 | 21/45 (LoVo, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.47× | +3.3 | 0.14 | 16/47 (BT-474, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.20 | 14/45 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.20 | 10/47 (SW480, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14056.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.457×** | -6.6 | 2e-08 | 41/47 (RPMI-7951, AN3 CA, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.464×** | -6.5 | 2e-08 | 39/48 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.469×** | -6.2 | 1e-07 | 35/46 (HEC-1-A, BT-474, …) | rises with dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.594×** | -5.8 | 1e-06 | 32/46 (HEC-1-A, BT-474, …) | rises with dose | composition shift; position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **0.567×** | -4.4 | 0.001 | 26/46 (NCI-H1573, LS 180, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.604×** | -4.3 | 0.002 | 24/47 (COLO 205, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 0.5 µM |  | **0.646×** | -3.7 | 0.018 | 19/46 (CFPAC-1, KATO III, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.664×** | -3.5 | 0.038 | 19/48 (KATO III, SW480, …) | inconsistent across doses | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.659×** | -3.4 | 0.044 | 21/45 (LoVo, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.682×** | -3.2 | 0.069 | 21/47 (NCI-H2030, A-427, …) | two highest doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.685×** | -3.2 | 0.071 | 19/47 (CFPAC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.672×** | -3.1 | 0.090 | 20/45 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14056. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[NCI-H1573 (line)]] | alt | 10.9 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0858× (z -12.4) |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -8.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW480 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.218× (z -9.3) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14056), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRWD1]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[MBD3]] | +0.67 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LINC00106]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 | same gene group; ⚠ same locus (2.4 kb, same strand: neighbours can correlate without regulation) |
| [[PPAN]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[KLHDC4]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[WDR4]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZBTB47]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NOM1]] | +0.61 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[TWNK]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NCL]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ALG8]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[BRD9]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC1P2]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[UBR2]] | -0.56 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CCNI]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LINC00888-1]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[MINDY2]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CRBN]] | -0.54 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[DCP2]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[HADHB]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ANKMY2]] | -0.51 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[KBTBD3]] | -0.51 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[TMEM167B]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[UBE2B]] | -0.50 | -0.48 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRABD2B]] | B | TRABD2B activity raises ASMTL-AS1's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without TRABD2B | 0.083 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.6, -30.1); signed map (6.8, -52.9). **Vector** length 73.6, 12.6% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.9 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.0 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -2.6 | -5.8 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.3 | -6.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -4.3 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ASMTL antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xp22.33 and Yp11.32 — chrX:1,401,769-1,414,028 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ13330; previously CXYorf2, NCRNA00105, ASMTLAS, ASMTL-AS |
| Gene groups (HGNC) | Pseudoautosomal region 1; Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [80161](https://www.ncbi.nlm.nih.gov/gene/80161):

> This gene serves as the antisense to the acetylserotonin O-methyltransferase-like gene. Multiple non-coding transcript variants have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:25811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25811) · Entrez [80161](https://www.ncbi.nlm.nih.gov/gene/80161) · Ensembl [ENSG00000236017](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236017)

## Data

Gene col 14056: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14056); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14056, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14056]; `tensor/DDL_lfc|DDL_z.npy` [14056]; `embed/gene_vectors.npy` [14056]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14056 or target_col == 14056). Every well: [[ASMTL-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASMTL-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

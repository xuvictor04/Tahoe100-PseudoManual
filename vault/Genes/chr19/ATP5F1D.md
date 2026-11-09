---
symbol: "ATP5F1D"
type: "gene"
col: 1806
ensembl_id: "ENSG00000099624"
name: "ATP synthase F1 subunit delta"
location: "19p13.3"
module: 58
arm: "+"
pooled_cpm: 18.65
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# ATP5F1D

*ATP synthase F1 subunit delta* — 19p13.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.28× (z +9.2, q 3e-17, up in 40 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 8.39×, LoVo 5.88×, NCI-H1792 9.96×, PANC-1 4.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 9.34×, SW480 6.57×, KATO III 6.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.253×, AsPC-1 0.232×; ⚠ cell-cycle shift, would explain all of this change); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (SNU-423 0.0459×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 32 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA10]] (+0.74, fdr 5e-05, ⚠ NAA10 in the vector space only through flagged drug-doses), [[ANTKMT]] (+0.72, fdr 4e-04), [[RPS26]] (+0.71, fdr 3e-05), [[POLR2I]] (+0.71, fdr 8e-05); moves opposite to [[EIF4G2]] (-0.69, fdr 1e-04), [[ATXN1L]] (-0.63, fdr 6e-04), [[MOB1A]] (-0.60, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1806.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 8.39×, LoVo 5.88×, NCI-H1792 9.96×, PANC-1 4.72×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 9.34×, SW480 6.57×, KATO III 6.00×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **4.28×** | +9.2 | 3e-17 | 40/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.54×** | +7.7 | 5e-12 | 28/31 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.61×** | +5.6 | 4e-06 | 30/33 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.6 | 0.045 | 27/42 (MIA PaCa-2, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.71×** | +3.4 | 0.082 | 27/43 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.22 | 21/48 (LOX-IMVI, SW480, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.253×, AsPC-1 0.232×; ⚠ cell-cycle shift, would explain all of this change); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (SNU-423 0.0459×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 13.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.34× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW480 (line)]] | alt | 18.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.57× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.253× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.232× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0459× (z -12.9) |
| [[A-172 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 27 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA10]] ⚠ | +0.74 | +0.40 / +0.72 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANTKMT]] | +0.72 | +0.24 / +0.71 | both halves | 4e-04 |  |
| [[RPS26]] | +0.71 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[POLR2I]] | +0.71 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[PAXX]] ⚠ | +0.70 | +0.33 / +0.68 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL14]] | +0.70 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[ELOB]] | +0.70 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.69 | +0.43 / +0.65 | both halves | 3e-05 | pathway: Cristae formation; STRING 513 |
| [[TMEM256]] | +0.69 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[C4orf48]] | +0.69 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[ATP5ME]] | +0.69 | +0.51 / +0.66 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX5A]] ⚠ | +0.68 | +0.56 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 980; ⚠ in the vector space only through flagged drug-doses |
| [[LSM2]] | +0.68 | +0.37 / +0.64 | both halves | 9e-05 |  |
| [[UQCR11]] | +0.66 | +0.53 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 922 |
| [[ANAPC11]] | +0.66 | +0.28 / +0.58 | both halves | 3e-04 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.69 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[ATXN1L]] | -0.63 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[MOB1A]] | -0.60 | -0.29 / -0.66 | both halves | 2e-04 |  |
| [[PBLD]] | -0.59 | -0.15 / -0.28 | ⚠ not reproduced | 0.001 |  |
| [[VPS52]] | -0.59 | -0.20 / -0.37 | ⚠ not reproduced | 8e-04 |  |
| [[PSME3IP1]] | -0.59 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[UBE2A]] | -0.59 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.58 | -0.05 / -0.39 | ⚠ not reproduced | 0.005 |  |
| [[SEPTIN8]] | -0.58 | -0.20 / -0.41 | both halves | 7e-04 |  |
| [[NXT2]] | -0.58 | -0.24 / -0.41 | both halves | 5e-04 |  |
| [[NCSTN]] | -0.58 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[DVL3]] | -0.57 | -0.13 / -0.59 | ⚠ one half (not replicated) | 0.002 |  |
| [[RNF6]] | -0.56 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[METTL4]] | -0.56 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[PGRMC1]] | -0.55 | -0.31 / -0.59 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.763). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.5, -15.7); signed map (-32.1, 4.7). **Vector** length 50.8, 12.0% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | -0.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +0.9 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase F1 subunit delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,241,746-1,244,825 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ATP5D |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P30049](https://www.uniprot.org/uniprotkb/P30049) (ATP synthase F(1) complex subunit delta, mitochondrial):

> Subunit delta, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and …

**Summary**, from NCBI Gene [513](https://www.ncbi.nlm.nih.gov/gene/513):

> This gene encodes a subunit of mitochondrial ATP synthase. Mitochondrial ATP synthase catalyzes ATP synthesis, utilizing an electrochemical gradient of protons across the inner membrane during oxidative phosphorylation. ATP synthase is composed of two linked multi-subunit complexes: the soluble catalytic core, F1, and the membrane-spanning component, Fo, comprising the proton channel. The catalytic portion of mitochondrial ATP synthase consists of 5 different subunits (alpha, beta, gamma, …

**Accessions** — [HGNC:837](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:837) · Entrez [513](https://www.ncbi.nlm.nih.gov/gene/513) · UniProt [P30049](https://www.uniprot.org/uniprotkb/P30049) · Ensembl [ENSG00000099624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099624)

## Data

Gene col 1806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1806); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1806]; `tensor/DDL_lfc|DDL_z.npy` [1806]; `embed/gene_vectors.npy` [1806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1806 or target_col == 1806). Every well: [[ATP5F1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5F1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

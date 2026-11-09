---
symbol: "ZMAT3"
type: "gene"
col: 10280
ensembl_id: "ENSG00000172667"
name: "zinc finger matrin-type 3"
location: "3q26.32"
module: 62
arm: "+"
pooled_cpm: 38.4
n_lines_expressing: 45
n_dd_up: 36
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# ZMAT3

*zinc finger matrin-type 3* — 3q26.32

> [!summary] In one line
> ZMAT3 is a zinc-finger RNA-binding protein, induced by p53 about as reliably as any gene in the pathway, which acts on its targets' splicing and stability rather than on their transcription.

## What it is

ZMAT3 — zinc finger matrin-type 3, known in the older literature as Wig-1 and PAG608 — was found in the 1990s as a p53-inducible gene encoding a nuclear protein with three matrin-type zinc fingers. Those fingers bind RNA, including double-stranded RNA, and everything ZMAT3 is thought to do is post-transcriptional.

Two mechanistic accounts exist, and they are not the same claim. The earlier one is stability: Wig-1 was reported to bind AU-rich elements in 3′ untranslated regions and to stabilise its targets, p53 mRNA itself among them, which would make it a positive-feedback element in the pathway. The later and better-supported account is splicing. *In vivo* RNAi and CRISPR screens in Kras-driven mouse lung and liver tumours converged on Zmat3 as a tumour suppressor acting downstream of p53; ZMAT3 was then shown to bind thousands of pre-mRNAs, mostly at intronic uridine-rich sequences, and to change exon inclusion in ways frequently coupled to nonsense-mediated decay. Among the transcripts it acts on are the p53 inhibitors [[MDM2]] and [[MDM4]]. Independent work in colorectal cells found CD44 its strongest alternatively spliced target: losing ZMAT3 shifts CD44 toward the oncogenic variant isoforms, and knocking those variants down rescues the growth advantage ZMAT3 loss confers.

## What is uncertain

The vault's curated table files ZMAT3 under negative feedback, and that label does not sit comfortably with either mechanistic account: stabilising p53 mRNA would be positive feedback, and shifting MDM2 and MDM4 transcripts toward nonsense-mediated decay would also relieve inhibition of p53. Read the label as inherited annotation, not a conclusion, and do not infer the sign of ZMAT3's effect on p53 from it.

The two mechanisms are themselves unreconciled — different binding preferences, different consequences — and the later papers treat the AU-rich-element proposal as prior work, not something they confirmed. The tumour-suppressor genetics are strong but come from particular mouse models and cell lines. And in a transcript-level dataset ZMAT3 mRNA reports that p53 fired, not that ZMAT3 did anything to its RNA targets; the splicing output would need isoform-level quantification that 3′-biased single-cell data cannot supply.

## References

- Varmeh-Ziaie et al., 1997, *Oncogene* — identified Wig-1 as a p53-induced zinc-finger gene.
- Hellborg et al., 2001, *Oncogene* — characterised human Wig-1 as a p53-induced, growth-inhibitory nuclear protein with three zinc fingers.
- Méndez-Vidal et al., 2002, *Nucleic Acids Research* — showed Wig-1 binds double-stranded RNA with high affinity, the first zinc finger being required.
- Vilborg et al., 2009, *PNAS* — reported that Wig-1 binds an AU-rich element in the p53 3′ UTR and stabilises p53 mRNA.
- Bieging-Rolett et al., 2020, *Molecular Cell* — screens identified Zmat3 as a p53-dependent tumour suppressor and showed it regulates splicing, including of MDM2 and MDM4, with coupling to nonsense-mediated decay.
- Muys et al., 2021, *Genes & Development* — showed ZMAT3 binds intronic uridine-rich regions and suppresses inclusion of oncogenic CD44 variant exons, defining a p53–ZMAT3–CD44 axis.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +21.7, q 0e+00, up in 40 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.766× (z -4.6, q 0.003, down in 20 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (LOX-IMVI 0.326×, A-427 0.364×, NCI-H2347 0.372×, A498 0.347×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.337×, SNU-1 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA18]] (+0.83, fdr 7e-06), [[ACTA2]] (+0.80, fdr 7e-06), [[EDA2R]] (+0.79, fdr 7e-06); moves opposite to [[RUVBL2]] (-0.51, fdr 5e-05), [[POLR1E]] (-0.47, fdr 1e-04), [[PWWP3A]] (-0.45, fdr 2e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 3 go from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +21.7 | 0e+00 | 40/43 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +16.4 | 0e+00 | 32/43 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.47×** | +15.3 | 0e+00 | 38/43 (NCI-H23, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +14.3 | 2e-44 | 33/39 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +12.3 | 7e-33 | 28/43 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +12.0 | 3e-31 | 37/44 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +11.7 | 8e-30 | 31/43 (LOX-IMVI, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.82×** | +10.2 | 2e-22 | 23/43 (SK-MEL-2, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.82×** | +10.2 | 2e-22 | 23/42 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.74×** | +9.3 | 6e-19 | 23/43 (SK-MEL-2, HEC-1-A, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +9.2 | 1e-18 | 25/43 (SNU-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.74×** | +9.0 | 1e-17 | 29/42 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.73×** | +8.9 | 3e-17 | 31/41 (RKO, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.72×** | +8.8 | 4e-17 | 27/42 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.68×** | +8.7 | 9e-17 | 20/28 (LOX-IMVI, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +7.6 | 8e-13 | 23/42 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +7.4 | 3e-12 | 22/42 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.4 | 6e-12 | 20/42 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +7.0 | 5e-11 | 28/43 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +5.9 | 9e-08 | 20/43 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +5.8 | 2e-07 | 24/43 (LS 180, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.2 | 5e-06 | 20/43 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 6 lines (LOX-IMVI 0.326×, A-427 0.364×, NCI-H2347 0.372×, A498 0.347×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.337×, SNU-1 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -4.6 | 0.003 | 20/42 (LOX-IMVI, A-427, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.819× | -3.4 | 0.17 | 8/42 (LS 180, C32, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.836× | -3.1 | 0.39 | 7/43 (LoVo, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 93.1 | 11 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +14.2) | [[Auranofin (drug)]] 5 µM 0.347× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 46.6 | 11 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +16.9) | — |
| [[RKO (line)]] | wt | 69.3 | 11 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +17.7) | — |
| [[A-172 (line)]] | wt | 84.5 | 9 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 80.3 | 8 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +14.4) | [[Auranofin (drug)]] 5 µM 0.326× (z -11.4) |
| [[A-427 (line)]] | wt | 82.6 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.9) | [[Auranofin (drug)]] 5 µM 0.364× (z -11.0) |
| [[LS 180 (line)]] | wt | 63.7 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +15.9) | — |
| [[LoVo (line)]] | wt | 50.0 | 5 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.315× (z -9.1) |
| [[SNU-1 (line)]] | wt | 72.9 | 5 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 4.72× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW48 (line)]] | wt | 80.6 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.04× (z +12.0) | — |
| [[SW480 (line)]] | alt | 21.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.1) | — |
| [[H4 (line)]] | wt | 99.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 35.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +27.8) | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 10.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +17.3) | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.2) | — |
| [[A549 (line)]] | wt | 41.7 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.28× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +8.9) | — |
| [[C32 (line)]] | wt | 119 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.300× (z -8.5) |
| [[PANC-1 (line)]] | alt | 27.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 20.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +16.1) | — |
| [[J82 (line)]] | alt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +15.2) | — |
| [[KATO III (line)]] | alt | 18.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.28× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 65.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.6) | [[Auranofin (drug)]] 5 µM 0.372× (z -10.0) |
| [[C-33 A (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.42× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 149 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.42× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 55.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +13.9) | — |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.00 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.48 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA18]] | +0.83 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[ACTA2]] | +0.80 | +0.81 / +0.78 | both halves | 7e-06 | STRING 423 |
| [[EDA2R]] | +0.79 | +0.62 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PINCR]] | +0.75 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[MDM2]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 520 |
| [[FDXR]] | +0.75 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 485 |
| [[PTCHD4]] | +0.74 | +0.63 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2C]] | +0.74 | +0.66 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[RRM2B]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 | STRING 495 |
| [[FAS]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PURPL]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[TP53INP1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUVBL2]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[POLR1E]] | -0.47 | -0.32 / -0.45 | both halves | 1e-04 |  |
| [[PWWP3A]] | -0.45 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[TUBA1C]] | -0.45 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[FARP2]] | -0.43 | -0.39 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 2, B 13, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens ZMAT3's drug response | recorded loss-of-function mutation of TP53 in 28 lines vs 16 not recorded | the TP53-altered lines respond 1.09× as strongly (z diff -0.64); strongest at Mitoxantrone (dihydrochloride) 5 µM: 1.38x vs 2.38x (z diff +6.4) | 0.003 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |
| [[TP53]] | A | TP53 activity raises ZMAT3's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 3.32× lower at baseline in the TP53-altered lines | 0.048 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[EDA2R]] | B | EDA2R activity raises ZMAT3's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without EDA2R | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PTCHD4]] | B | PTCHD4 activity raises ZMAT3's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 3.35× lower at baseline in the lines without PTCHD4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity raises ZMAT3's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.98× lower at baseline in the lines without PINCR | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[PINCR]] | B | PINCR activity weakens ZMAT3's drug response | lines that do not express PINCR (25) vs lines expressing it (19) | the lines without PINCR respond 1.16× as strongly (z diff -0.62); strongest at Panobinostat 0.5 µM: 2.44x vs 0.86x (z diff -6.2) | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ZMAT3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises ZMAT3's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 2.72× lower at baseline in the lines without GRIN2C | 0.010 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[CYFIP2]] | B | CYFIP2 activity raises ZMAT3's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without CYFIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[FDXR]] | B | FDXR activity raises ZMAT3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.54× lower at baseline in the lines without FDXR | 0.017 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[PTCHD4]] | B | PTCHD4 activity weakens ZMAT3's drug response | lines that do not express PTCHD4 (28) vs lines expressing it (16) | the lines without PTCHD4 respond 1.43× as strongly (z diff -1.04); strongest at Panobinostat 0.5 µM: 2.21x vs 0.84x (z diff -5.9) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[TP53INP1]] | B | TP53INP1 activity raises ZMAT3's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 2.29× lower at baseline in the lines without TP53INP1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | ZMAT3's natural level strengthens FBXO22's drug response | ZMAT3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse -0.34; direction not clear | 0.010 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MDM2]] | C | ZMAT3's natural level strengthens MDM2's drug response | ZMAT3's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.74, reverse -0.36; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ACTA2]] | C | ZMAT3's natural level strengthens ACTA2's drug response | ZMAT3's natural level across 32 lines (lineage-adjusted; a glimpse) | r +0.78, reverse -0.53; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.9, 36.5); signed map (42.5, -23.9). **Vector** length 118, 34.6% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.62 to 6); *apoptosis* (hallmark, mean cos +0.61 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +14.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.8 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +5.2 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +11.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.7 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.5 | -4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.8 | +10.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.0 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.3 | +10.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger matrin-type 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.32 — chr3:178,960,121-179,072,215 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WIG1, MGC10613, FLJ12296, WIG-1, PAG608 |
| Gene groups (HGNC) | Zinc fingers matrin-type |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HA38](https://www.uniprot.org/uniprotkb/Q9HA38) (Zinc finger matrin-type protein 3):

> Acts as a bona fide target gene of p53/TP53. May play a role in the TP53-dependent growth regulatory pathway. May contribute to TP53-mediated apoptosis by regulation of TP53 expression and translocation to the nucleus and nucleolus.

**Summary**, from NCBI Gene [64393](https://www.ncbi.nlm.nih.gov/gene/64393):

> This gene encodes a protein containing three zinc finger domains and a nuclear localization signal. The mRNA and the protein of this gene are upregulated by wildtype p53 and overexpression of this gene inhibits tumor cell growth, suggesting that this gene may have a role in the p53-dependent growth regulatory pathway. Alternative splicing of this gene results in two transcript variants encoding two isoforms differing in only one amino acid. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:29983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29983) · Entrez [64393](https://www.ncbi.nlm.nih.gov/gene/64393) · UniProt [Q9HA38](https://www.uniprot.org/uniprotkb/Q9HA38) · Ensembl [ENSG00000172667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172667)

## Data

Gene col 10280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10280); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10280]; `tensor/DDL_lfc|DDL_z.npy` [10280]; `embed/gene_vectors.npy` [10280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10280 or target_col == 10280). Every well: [[ZMAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ZMAT3.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
